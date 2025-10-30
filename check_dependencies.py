#!/usr/bin/env python3
"""
Script de verificación de dependencias para NetGui
"""
import sys
import subprocess


def check_command(command: str, description: str) -> bool:
    """Verifica si un comando existe en el sistema"""
    try:
        result = subprocess.run(
            ['which', command],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode == 0:
            print(f"✓ {description}: {result.stdout.strip()}")
            return True
        else:
            print(f"✗ {description}: NO ENCONTRADO")
            return False
    except Exception as e:
        print(f"✗ {description}: ERROR - {e}")
        return False


def check_python_package(package: str, description: str) -> bool:
    """Verifica si un paquete Python está instalado"""
    try:
        __import__(package)
        print(f"✓ {description}")
        return True
    except ImportError:
        print(f"✗ {description}: NO INSTALADO")
        return False


def check_service(service: str, description: str) -> bool:
    """Verifica si un servicio está activo"""
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', service],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode == 0 and result.stdout.strip() == 'active':
            print(f"✓ {description}: ACTIVO")
            return True
        else:
            print(f"✗ {description}: INACTIVO")
            return False
    except Exception as e:
        print(f"✗ {description}: ERROR - {e}")
        return False


def main():
    print("=" * 60)
    print("NetGui - Verificación de Dependencias")
    print("=" * 60)
    print()
    
    all_ok = True
    
    # Verificar comandos del sistema
    print("Comandos del sistema:")
    print("-" * 60)
    all_ok &= check_command('nmcli', 'NetworkManager CLI')
    all_ok &= check_command('nm-connection-editor', 'NetworkManager Editor GUI')
    all_ok &= check_command('python3', 'Python 3')
    print()
    
    # Verificar servicios
    print("Servicios del sistema:")
    print("-" * 60)
    all_ok &= check_service('NetworkManager', 'NetworkManager')
    print()
    
    # Verificar paquetes Python
    print("Paquetes Python:")
    print("-" * 60)
    all_ok &= check_python_package('PyQt6', 'PyQt6')
    all_ok &= check_python_package('PyQt6.QtWidgets', 'PyQt6.QtWidgets')
    all_ok &= check_python_package('PyQt6.QtCore', 'PyQt6.QtCore')
    all_ok &= check_python_package('PyQt6.QtGui', 'PyQt6.QtGui')
    print()
    
    # Verificar archivos del proyecto
    print("Archivos del proyecto:")
    print("-" * 60)
    import os
    files_to_check = [
        'main.py',
        'network_manager.py',
        'requirements.txt',
        'README.md'
    ]
    
    for file in files_to_check:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file}: NO ENCONTRADO")
            all_ok = False
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✓ TODAS LAS DEPENDENCIAS ESTÁN CORRECTAMENTE INSTALADAS")
        print()
        print("Puedes ejecutar NetGui con:")
        print("  python3 main.py")
        return 0
    else:
        print("✗ FALTAN ALGUNAS DEPENDENCIAS")
        print()
        print("Instrucciones:")
        print("1. Dependencias del sistema:")
        print("   sudo apt install network-manager python3 python3-pip python3-venv network-manager-gnome")
        print()
        print("2. Dependencias Python (si no estás en venv):")
        print("   python3 -m venv venv")
        print("   source venv/bin/activate")
        print("   pip install -r requirements.txt")
        return 1
    
    print("=" * 60)


if __name__ == '__main__':
    sys.exit(main())

