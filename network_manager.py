#!/usr/bin/env python3
"""
NetworkManager - Módulo para gestionar perfiles de red usando NetworkManager
"""
import subprocess
import json
import re
from typing import List, Dict, Optional


class NetworkProfile:
    """Representa un perfil de conexión de red"""
    def __init__(self, uuid: str, name: str, connection_type: str, device: str = ""):
        self.uuid = uuid
        self.name = name
        self.connection_type = connection_type
        self.device = device
        self.is_active = False
    
    def __repr__(self):
        return f"NetworkProfile(name={self.name}, type={self.connection_type}, active={self.is_active})"


class NetworkManager:
    """Gestor de perfiles de red usando NetworkManager"""
    
    @staticmethod
    def run_command(command: List[str]) -> tuple[bool, str]:
        """Ejecuta un comando del sistema y retorna el resultado"""
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            return False, e.stderr
    
    @staticmethod
    def get_profiles() -> List[NetworkProfile]:
        """Obtiene lista de todos los perfiles de red"""
        success, output = NetworkManager.run_command([
            'nmcli', '-t', '-f', 'UUID,NAME,TYPE,DEVICE', 'connection', 'show'
        ])
        
        if not success:
            return []
        
        profiles = []
        for line in output.strip().split('\n'):
            if not line:
                continue
            parts = line.split(':')
            if len(parts) >= 3:
                uuid = parts[0]
                name = parts[1]
                conn_type = parts[2]
                device = parts[3] if len(parts) > 3 else ""
                profile = NetworkProfile(uuid, name, conn_type, device)
                profiles.append(profile)
        
        # Obtener conexiones activas
        active_uuids = NetworkManager.get_active_connections()
        for profile in profiles:
            if profile.uuid in active_uuids:
                profile.is_active = True
        
        return profiles
    
    @staticmethod
    def get_active_connections() -> set:
        """Obtiene los UUIDs de las conexiones activas"""
        success, output = NetworkManager.run_command([
            'nmcli', '-t', '-f', 'UUID', 'connection', 'show', '--active'
        ])
        
        if not success:
            return set()
        
        return set(line.strip() for line in output.strip().split('\n') if line)
    
    @staticmethod
    def get_profile_details(uuid: str) -> Dict[str, str]:
        """Obtiene detalles de un perfil específico"""
        success, output = NetworkManager.run_command([
            'nmcli', 'connection', 'show', uuid
        ])
        
        if not success:
            return {}
        
        details = {}
        for line in output.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                details[key.strip()] = value.strip()
        
        return details
    
    @staticmethod
    def duplicate_profile(uuid: str, new_name: str) -> tuple[bool, str]:
        """Duplica un perfil de red"""
        # Primero obtenemos el perfil original
        success, output = NetworkManager.run_command([
            'nmcli', 'connection', 'clone', uuid, new_name
        ])
        
        if success:
            # Extraer el UUID del nuevo perfil del output
            match = re.search(r'\(([a-f0-9-]+)\)', output)
            if match:
                new_uuid = match.group(1)
                return True, new_uuid
            return True, "Perfil duplicado exitosamente"
        
        return False, output
    
    @staticmethod
    def delete_profile(uuid: str) -> tuple[bool, str]:
        """Elimina un perfil de red"""
        success, output = NetworkManager.run_command([
            'nmcli', 'connection', 'delete', uuid
        ])
        
        return success, output if success else "Error al eliminar el perfil"
    
    @staticmethod
    def activate_profile(uuid: str, interface: Optional[str] = None) -> tuple[bool, str]:
        """Activa un perfil de red específico"""
        cmd = ['nmcli', 'connection', 'up', uuid]
        if interface:
            cmd.extend(['ifname', interface])
        
        success, output = NetworkManager.run_command(cmd)
        return success, output if success else "Error al activar el perfil"
    
    @staticmethod
    def deactivate_profile(uuid: str) -> tuple[bool, str]:
        """Desactiva un perfil de red"""
        success, output = NetworkManager.run_command([
            'nmcli', 'connection', 'down', uuid
        ])
        
        return success, output if success else "Error al desactivar el perfil"
    
    @staticmethod
    def modify_profile(uuid: str, settings: Dict[str, str]) -> tuple[bool, str]:
        """Modifica configuración de un perfil"""
        for key, value in settings.items():
            cmd = ['nmcli', 'connection', 'modify', uuid, key, value]
            success, output = NetworkManager.run_command(cmd)
            if not success:
                return False, f"Error al modificar {key}: {output}"
        
        return True, "Perfil modificado exitosamente"
    
    @staticmethod
    def get_devices() -> List[str]:
        """Obtiene lista de dispositivos de red disponibles"""
        success, output = NetworkManager.run_command([
            'nmcli', '-t', '-f', 'DEVICE', 'device'
        ])
        
        if not success:
            return []
        
        devices = [line.strip() for line in output.strip().split('\n') if line.strip()]
        return [d for d in devices if d and d != '--']
    
    @staticmethod
    def restart_interface(interface: str) -> tuple[bool, str]:
        """Reinicia una interfaz de red"""
        # Primero bajamos la interfaz
        success1, _ = NetworkManager.run_command([
            'nmcli', 'device', 'disconnect', interface
        ])
        
        # Luego la levantamos
        success2, output = NetworkManager.run_command([
            'nmcli', 'device', 'connect', interface
        ])
        
        if success2:
            return True, f"Interfaz {interface} reiniciada exitosamente"
        else:
            return False, f"Error al reiniciar la interfaz: {output}"
    
    @staticmethod
    def open_connection_editor(uuid: Optional[str] = None) -> bool:
        """Abre nm-connection-editor para editar una conexión"""
        try:
            if uuid:
                subprocess.Popen(['nm-connection-editor', '--edit', uuid])
            else:
                subprocess.Popen(['nm-connection-editor'])
            return True
        except Exception as e:
            print(f"Error al abrir nm-connection-editor: {e}")
            return False
    
    @staticmethod
    def get_current_ip_info() -> Dict[str, str]:
        """Obtiene información de IP actual de todas las interfaces activas"""
        # Obtener dispositivos conectados
        success, output = NetworkManager.run_command([
            'nmcli', '-t', '-f', 'DEVICE,TYPE,STATE', 'device'
        ])
        
        if not success:
            return {}
        
        info = {}
        
        # Procesar cada dispositivo
        for line in output.strip().split('\n'):
            if not line:
                continue
            
            parts = line.split(':')
            if len(parts) >= 3:
                device = parts[0]
                dev_type = parts[1]
                state = parts[2]
                
                # Solo procesar dispositivos conectados
                if 'connected' not in state.lower() or device == '--':
                    continue
                
                # Obtener información detallada del dispositivo
                success_detail, detail_output = NetworkManager.run_command([
                    'nmcli', '-t', '-f', 'IP4.ADDRESS,IP4.GATEWAY,IP4.DNS', 'device', 'show', device
                ])
                
                if success_detail:
                    device_info = {
                        'device': device,
                        'type': dev_type,
                        'state': state,
                        'ip': '',
                        'gateway': '',
                        'dns': ''
                    }
                    
                    for detail_line in detail_output.strip().split('\n'):
                        if not detail_line:
                            continue
                        
                        if detail_line.startswith('IP4.ADDRESS'):
                            ip = detail_line.split(':', 1)[1].strip() if ':' in detail_line else ''
                            if ip:
                                if device_info['ip']:
                                    device_info['ip'] += ', ' + ip
                                else:
                                    device_info['ip'] = ip
                        elif detail_line.startswith('IP4.GATEWAY'):
                            gateway = detail_line.split(':', 1)[1].strip() if ':' in detail_line else ''
                            if gateway:
                                device_info['gateway'] = gateway
                        elif detail_line.startswith('IP4.DNS'):
                            dns = detail_line.split(':', 1)[1].strip() if ':' in detail_line else ''
                            if dns:
                                if device_info['dns']:
                                    device_info['dns'] += ', ' + dns
                                else:
                                    device_info['dns'] = dns
                    
                    # Solo agregar si tiene al menos una IP
                    if device_info['ip']:
                        info[device] = device_info
        
        return info
    
    @staticmethod
    def get_primary_ip() -> str:
        """Obtiene la IP primaria del sistema"""
        success, output = NetworkManager.run_command([
            'hostname', '-I'
        ])
        
        if success and output.strip():
            # Retorna la primera IP
            ips = output.strip().split()
            return ips[0] if ips else "Sin IP"
        
        return "Sin IP"

