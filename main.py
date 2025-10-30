#!/usr/bin/env python3
"""
NetGui - Gestor gráfico de perfiles de red para KDE Plasma
"""
import sys
from typing import Optional
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QListWidgetItem, QMessageBox, QDialog,
    QLabel, QLineEdit, QFormLayout, QDialogButtonBox, QTextEdit,
    QGroupBox, QSplitter, QMenu, QFrame, QComboBox
)
from PyQt6.QtCore import Qt, QTimer, QUrl
from PyQt6.QtGui import QIcon, QAction, QFont, QDesktopServices
from network_manager import NetworkManager, NetworkProfile


class AboutDialog(QDialog):
    """Diálogo Acerca de NetGui"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Acerca de NetGui")
        self.setMinimumSize(500, 450)
        self.setMaximumSize(550, 500)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Logo y título
        title_label = QLabel("🌐 <b style='font-size: 24pt; color: #1976D2;'>NetGui</b>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("padding: 15px; background-color: #E3F2FD; border-radius: 8px;")
        layout.addWidget(title_label)
        
        # Versión
        version_label = QLabel("<p style='text-align: center; font-size: 14pt;'><b>Versión 1.2.1</b></p>")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version_label)
        
        # Descripción
        desc_text = QTextEdit()
        desc_text.setReadOnly(True)
        desc_text.setMaximumHeight(250)
        desc_html = """
        <div style='padding: 10px;'>
            <h3 style='color: #1976D2;'>Gestor de Perfiles de Red</h3>
            <p><b>NetGui</b> es una aplicación moderna para gestionar perfiles de red en Linux con KDE Plasma.</p>
            
            <h4>✨ Características:</h4>
            <ul>
                <li>📡 Monitor de red en tiempo real</li>
                <li>🔄 Cambio rápido entre perfiles</li>
                <li>📋 Duplicación y edición de perfiles</li>
                <li>✅ Validación de configuraciones</li>
                <li>🎨 Interfaz moderna y atractiva</li>
            </ul>
            
            <h4>💻 Tecnología:</h4>
            <p>
                <b>Backend:</b> NetworkManager (nmcli)<br>
                <b>Frontend:</b> PyQt6<br>
                <b>Sistema:</b> Debian 13 (Trixie) / KDE Plasma 6<br>
                <b>Python:</b> 3.11+
            </p>
            
            <h4>📄 Licencia:</h4>
            <p>CC BY-NC-SA 4.0 (No Comercial) © 2025</p>
            
            <p style='text-align: center; margin-top: 10px;'>
                <i>Desarrollado con ❤️ para la comunidad Linux</i>
            </p>
        </div>
        """
        desc_text.setHtml(desc_html)
        layout.addWidget(desc_text)
        
        # Botones
        button_layout = QHBoxLayout()
        
        docs_btn = QPushButton("📚 Documentación")
        docs_btn.clicked.connect(self.open_docs)
        docs_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #2196F3;
                border: 2px solid #2196F3;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #2196F3;
                color: white;
                border: 2px solid #2196F3;
            }
            QPushButton:pressed {
                background-color: #1976D2;
                border: 2px solid #1976D2;
            }
        """)
        button_layout.addWidget(docs_btn)
        
        close_btn = QPushButton("Cerrar")
        close_btn.clicked.connect(self.accept)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #607D8B;
                border: 2px solid #607D8B;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #607D8B;
                color: white;
                border: 2px solid #607D8B;
            }
            QPushButton:pressed {
                background-color: #455A64;
                border: 2px solid #455A64;
            }
        """)
        button_layout.addWidget(close_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def open_docs(self):
        """Abre la carpeta de documentación"""
        import os
        docs_path = os.path.join(os.path.dirname(__file__), 'documentacion')
        if os.path.exists(docs_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(docs_path))
        else:
            QMessageBox.information(
                self,
                "Documentación",
                "La documentación se encuentra en la carpeta 'documentacion' del proyecto.\n\n"
                "Consulta README.md para información completa."
            )


class ProfileDetailsDialog(QDialog):
    """Diálogo para mostrar detalles de un perfil"""
    def __init__(self, profile: NetworkProfile, parent=None):
        super().__init__(parent)
        self.profile = profile
        self.setWindowTitle(f"Detalles: {profile.name}")
        self.setMinimumSize(600, 400)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        details_text = QTextEdit()
        details_text.setReadOnly(True)
        
        # Obtener detalles del perfil
        details = NetworkManager.get_profile_details(self.profile.uuid)
        
        text = f"<h3>Perfil: {self.profile.name}</h3>"
        text += f"<p><b>UUID:</b> {self.profile.uuid}</p>"
        text += f"<p><b>Tipo:</b> {self.profile.connection_type}</p>"
        text += f"<p><b>Dispositivo:</b> {self.profile.device if self.profile.device else 'N/A'}</p>"
        text += f"<p><b>Estado:</b> {'Activo' if self.profile.is_active else 'Inactivo'}</p>"
        text += "<hr>"
        
        if details:
            text += "<h4>Configuración completa:</h4>"
            text += "<pre>"
            for key, value in sorted(details.items()):
                text += f"{key}: {value}\n"
            text += "</pre>"
        
        details_text.setHtml(text)
        layout.addWidget(details_text)
        
        # Botones
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)


class DuplicateDialog(QDialog):
    """Diálogo para duplicar un perfil"""
    def __init__(self, original_name: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Duplicar Perfil")
        self.setMinimumWidth(400)
        self.new_name = ""
        self.setup_ui(original_name)
    
    def setup_ui(self, original_name: str):
        layout = QFormLayout()
        
        self.name_input = QLineEdit(f"{original_name} (copia)")
        layout.addRow("Nombre del nuevo perfil:", self.name_input)
        
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addRow(button_box)
        
        self.setLayout(layout)
    
    def accept(self):
        self.new_name = self.name_input.text().strip()
        if not self.new_name:
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío")
            return
        super().accept()


class QuickEditDialog(QDialog):
    """Diálogo para edición rápida de parámetros comunes"""
    def __init__(self, profile: NetworkProfile, parent=None):
        super().__init__(parent)
        self.profile = profile
        self.setWindowTitle(f"Editar: {profile.name}")
        self.setMinimumWidth(500)
        self.settings = {}
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Información
        info_label = QLabel(
            "<b>Edición rápida de parámetros comunes</b><br>"
            "Para edición avanzada, usa el botón 'Editor Avanzado'"
        )
        layout.addWidget(info_label)
        
        # Formulario de configuración común
        form_layout = QFormLayout()
        
        # Nombre de conexión
        self.name_input = QLineEdit()
        form_layout.addRow("Nombre de conexión:", self.name_input)
        
        # IPv4
        ipv4_group = QGroupBox("Configuración IPv4")
        ipv4_layout = QFormLayout()
        
        # Dropdown para método IPv4
        self.ipv4_method = QComboBox()
        self.ipv4_method.addItem("(No cambiar)", "")
        self.ipv4_method.addItem("Automático - DHCP (recomendado)", "auto")
        self.ipv4_method.addItem("Manual - IP Fija", "manual")
        self.ipv4_method.addItem("Solo enlace local", "link-local")
        self.ipv4_method.addItem("Compartido con otras computadoras", "shared")
        self.ipv4_method.addItem("Deshabilitado", "disabled")
        self.ipv4_method.setCurrentIndex(0)
        ipv4_layout.addRow("Método IPv4:", self.ipv4_method)
        
        method_hint = QLabel(
            "<small><i>"
            "<b>Automático (DHCP):</b> El router asigna la IP automáticamente<br>"
            "<b>Manual:</b> Debes llenar IP, Gateway y DNS manualmente"
            "</i></small>"
        )
        method_hint.setWordWrap(True)
        ipv4_layout.addRow("", method_hint)
        
        self.ipv4_address = QLineEdit()
        self.ipv4_address.setPlaceholderText("ej: 192.168.1.100/24")
        ipv4_layout.addRow("Dirección IP:", self.ipv4_address)
        
        self.ipv4_gateway = QLineEdit()
        self.ipv4_gateway.setPlaceholderText("ej: 192.168.1.1")
        ipv4_layout.addRow("Puerta de enlace (Gateway):", self.ipv4_gateway)
        
        self.ipv4_dns = QLineEdit()
        self.ipv4_dns.setPlaceholderText("ej: 8.8.8.8,8.8.4.4 o 1.1.1.1")
        ipv4_layout.addRow("Servidores DNS:", self.ipv4_dns)
        
        ipv4_group.setLayout(ipv4_layout)
        layout.addWidget(ipv4_group)
        
        # Botones
        button_layout = QHBoxLayout()
        
        advanced_btn = QPushButton("Editor Avanzado (nm-connection-editor)")
        advanced_btn.clicked.connect(self.open_advanced_editor)
        button_layout.addWidget(advanced_btn)
        
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        button_layout.addWidget(button_box)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def open_advanced_editor(self):
        """Abre nm-connection-editor para edición avanzada"""
        NetworkManager.open_connection_editor(self.profile.uuid)
    
    def validate_ip_address(self, ip_str: str) -> bool:
        """Valida formato de dirección IP con máscara (ej: 192.168.1.100/24)"""
        if not ip_str:
            return True  # Vacío es válido (no cambiar)
        
        import re
        # Formato: xxx.xxx.xxx.xxx/xx o xxx.xxx.xxx.xxx
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})(\/\d{1,2})?$'
        match = re.match(pattern, ip_str)
        
        if not match:
            return False
        
        # Validar que cada octeto esté entre 0 y 255
        for i in range(1, 5):
            if int(match.group(i)) > 255:
                return False
        
        # Validar máscara de red si existe
        if match.group(5):
            mask = int(match.group(5)[1:])  # Quitar el /
            if mask > 32:
                return False
        
        return True
    
    def validate_gateway(self, gateway_str: str) -> bool:
        """Valida formato de gateway (ej: 192.168.1.1)"""
        if not gateway_str:
            return True  # Vacío es válido
        
        import re
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
        match = re.match(pattern, gateway_str)
        
        if not match:
            return False
        
        # Validar que cada octeto esté entre 0 y 255
        for i in range(1, 5):
            if int(match.group(i)) > 255:
                return False
        
        return True
    
    def validate_dns(self, dns_str: str) -> bool:
        """Valida servidores DNS (pueden ser múltiples separados por coma)"""
        if not dns_str:
            return True  # Vacío es válido
        
        # Separar por comas y validar cada DNS
        dns_list = [d.strip() for d in dns_str.split(',')]
        
        import re
        pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
        
        for dns in dns_list:
            match = re.match(pattern, dns)
            if not match:
                return False
            
            # Validar que cada octeto esté entre 0 y 255
            for i in range(1, 5):
                if int(match.group(i)) > 255:
                    return False
        
        return True
    
    def accept(self):
        """Recopila los cambios y cierra el diálogo"""
        # Obtener valores
        method_value = self.ipv4_method.currentData()
        ip_address = self.ipv4_address.text().strip()
        gateway = self.ipv4_gateway.text().strip()
        dns = self.ipv4_dns.text().strip()
        
        # Validar IP
        if ip_address and not self.validate_ip_address(ip_address):
            QMessageBox.warning(
                self,
                "IP Inválida",
                f"La dirección IP '{ip_address}' no es válida.\n\n"
                "Formato correcto: 192.168.1.100/24\n"
                "- Cada número debe estar entre 0 y 255\n"
                "- La máscara debe estar entre /0 y /32"
            )
            return
        
        # Validar Gateway
        if gateway and not self.validate_gateway(gateway):
            QMessageBox.warning(
                self,
                "Gateway Inválido",
                f"El gateway '{gateway}' no es válido.\n\n"
                "Formato correcto: 192.168.1.1\n"
                "- Cada número debe estar entre 0 y 255"
            )
            return
        
        # Validar DNS
        if dns and not self.validate_dns(dns):
            QMessageBox.warning(
                self,
                "DNS Inválido",
                f"Los servidores DNS '{dns}' no son válidos.\n\n"
                "Formato correcto: 8.8.8.8,8.8.4.4\n"
                "- Separa múltiples DNS con comas\n"
                "- Cada número debe estar entre 0 y 255"
            )
            return
        
        # Si el método es "manual", validar que se hayan ingresado los datos necesarios
        if method_value == 'manual':
            if not ip_address:
                QMessageBox.warning(
                    self,
                    "Datos Incompletos",
                    "Para usar IP fija (manual) debes especificar:\n\n"
                    "• Dirección IP (requerido)\n"
                    "• Gateway (recomendado)\n"
                    "• DNS (recomendado)\n\n"
                    "Ejemplo:\n"
                    "IP: 192.168.1.100/24\n"
                    "Gateway: 192.168.1.1\n"
                    "DNS: 8.8.8.8,8.8.4.4"
                )
                return
            
            # Advertir si falta gateway o DNS (pero no bloquear)
            if not gateway or not dns:
                reply = QMessageBox.question(
                    self,
                    "Advertencia",
                    "Has seleccionado IP fija (manual) pero falta:\n\n" +
                    ("• Gateway\n" if not gateway else "") +
                    ("• Servidores DNS\n" if not dns else "") +
                    "\n¿Deseas continuar de todas formas?\n\n"
                    "La conexión podría no funcionar correctamente sin estos datos.",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.No:
                    return
        
        # Nombre
        if self.name_input.text().strip():
            self.settings['connection.id'] = self.name_input.text().strip()
        
        # IPv4 - obtener el valor del dropdown (data asociado al item seleccionado)
        if method_value:  # Si no es "(No cambiar)"
            self.settings['ipv4.method'] = method_value
        
        # Para método manual, asegurar que se guarden los datos correctamente
        if method_value == 'manual':
            if ip_address:
                self.settings['ipv4.addresses'] = ip_address
            if gateway:
                self.settings['ipv4.gateway'] = gateway
            if dns:
                self.settings['ipv4.dns'] = dns
        else:
            # Para otros métodos, solo guardar si hay datos
            if ip_address:
                self.settings['ipv4.addresses'] = ip_address
            if gateway:
                self.settings['ipv4.gateway'] = gateway
            if dns:
                self.settings['ipv4.dns'] = dns
        
        super().accept()


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NetGui - Gestor de Perfiles de Red")
        self.setMinimumSize(950, 650)
        self.resize(1100, 700)  # Tamaño inicial recomendado
        self.profiles = []
        self.setup_ui()
        self.load_profiles()
        self.update_network_info()  # Actualización inicial
        
        # Actualización automática cada 5 segundos
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.load_profiles)
        self.refresh_timer.start(5000)
        
        # Timer para actualizar información de red
        self.info_timer = QTimer()
        self.info_timer.timeout.connect(self.update_network_info)
        self.info_timer.start(3000)
    
    def create_info_panel(self) -> QGroupBox:
        """Crea el panel de información de red actual"""
        group = QGroupBox("📡 Información de Red Actual")
        layout = QVBoxLayout()
        layout.setSpacing(4)  # Reducir espaciado entre elementos
        layout.setContentsMargins(10, 8, 10, 8)  # Reducir márgenes
        
        # Estilo del grupo
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                font-size: 10pt;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 6px;
                background-color: #f5f5f5;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2E7D32;
            }
        """)
        
        # Label para el perfil activo (más prominente)
        self.profile_label = QLabel("🔌 Perfil: <b>Cargando...</b>")
        profile_font = QFont()
        profile_font.setPointSize(11)
        profile_font.setBold(True)
        self.profile_label.setFont(profile_font)
        self.profile_label.setStyleSheet("color: #1976D2; padding: 3px;")
        self.profile_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        layout.addWidget(self.profile_label)
        
        # Separador después del perfil
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.Shape.HLine)
        separator1.setFrameShadow(QFrame.Shadow.Sunken)
        separator1.setStyleSheet("background-color: #BDBDBD; max-height: 1px;")
        layout.addWidget(separator1)
        
        # Crear labels para mostrar la información de red
        self.ip_label = QLabel("🌐 <b>IP:</b> Cargando...")
        self.gateway_label = QLabel("🚪 <b>Gateway:</b> Cargando...")
        self.dns_label = QLabel("🔍 <b>DNS:</b> Cargando...")
        self.interface_label = QLabel("🔌 <b>Interfaz:</b> Cargando...")
        
        # Aplicar estilo y fuente
        font = QFont()
        font.setPointSize(9)
        
        for label in [self.ip_label, self.gateway_label, self.dns_label, self.interface_label]:
            label.setFont(font)
            label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            label.setStyleSheet("padding: 2px; color: #424242;")
            layout.addWidget(label)
        
        group.setLayout(layout)
        group.setMaximumHeight(175)
        group.setMinimumHeight(150)
        
        return group
    
    def update_network_info(self):
        """Actualiza la información de red en el panel"""
        ip_info = NetworkManager.get_current_ip_info()
        
        # Obtener el perfil activo
        active_profile = None
        for profile in self.profiles:
            if profile.is_active and profile.device != 'lo':  # Ignorar loopback
                # Priorizar ethernet y wifi sobre bridges
                if profile.connection_type in ['802-3-ethernet', '802-11-wireless', 'wifi', 'ethernet']:
                    active_profile = profile
                    break
        
        # Si no encontramos ethernet/wifi, tomar el primero activo que no sea loopback
        if not active_profile:
            for profile in self.profiles:
                if profile.is_active and profile.device != 'lo':
                    active_profile = profile
                    break
        
        # Actualizar label del perfil activo
        if active_profile:
            self.profile_label.setText(f"🔌 <b style='font-size: 13pt; color: #1976D2;'>Perfil Activo: {active_profile.name}</b>")
            self.profile_label.setStyleSheet("color: #1976D2; padding: 5px; background-color: #E3F2FD; border-radius: 4px;")
        else:
            self.profile_label.setText("🔌 <b>Perfil:</b> <span style='color: #F44336;'>Sin conexión activa</span>")
            self.profile_label.setStyleSheet("color: #757575; padding: 5px; background-color: #FFEBEE; border-radius: 4px;")
        
        if not ip_info:
            self.ip_label.setText("🌐 <b>IP:</b> <span style='color: #757575;'>Sin conexión activa</span>")
            self.gateway_label.setText("🚪 <b>Gateway:</b> <span style='color: #757575;'>N/A</span>")
            self.dns_label.setText("🔍 <b>DNS:</b> <span style='color: #757575;'>N/A</span>")
            self.interface_label.setText("🔌 <b>Interfaz:</b> <span style='color: #757575;'>N/A</span>")
            return
        
        # Obtener información del primer dispositivo conectado
        # Si hay múltiples, mostrar el más relevante (ethernet primero, luego wifi)
        devices = list(ip_info.keys())
        
        # Priorizar ethernet sobre wifi
        primary_device = None
        for device in devices:
            if 'eth' in device or 'enp' in device or 'eno' in device:
                primary_device = device
                break
        
        if not primary_device and devices:
            primary_device = devices[0]
        
        if primary_device:
            info = ip_info[primary_device]
            
            # Formatear y mostrar la información con colores
            ip_text = f"🌐 <b>IP:</b> <span style='color: #2E7D32; font-weight: bold;'>{info['ip'] if info['ip'] else 'N/A'}</span>"
            gateway_text = f"🚪 <b>Gateway:</b> <span style='color: #1565C0;'>{info['gateway'] if info['gateway'] else 'N/A'}</span>"
            dns_text = f"🔍 <b>DNS:</b> <span style='color: #6A1B9A;'>{info['dns'] if info['dns'] else 'N/A'}</span>"
            
            # Iconos según el tipo de interfaz
            interface_icon = "📡" if 'wl' in info['device'] or 'wifi' in info['type'] else "🔌"
            interface_text = f"{interface_icon} <b>Interfaz:</b> <span style='color: #E65100;'>{info['device']}</span> <span style='color: #757575;'>({info['type']}) - {info['state']}</span>"
            
            self.ip_label.setText(ip_text)
            self.gateway_label.setText(gateway_text)
            self.dns_label.setText(dns_text)
            self.interface_label.setText(interface_text)
            
            # Si hay múltiples dispositivos, agregarlo al tooltip
            if len(devices) > 1:
                tooltip = "🌐 Múltiples interfaces activas:\n\n"
                for dev in devices:
                    d_info = ip_info[dev]
                    tooltip += f"• {dev} ({d_info['type']}): {d_info['ip']}\n"
                self.ip_label.setToolTip(tooltip)
        else:
            self.ip_label.setText("🌐 <b>IP:</b> <span style='color: #F44336;'>Sin conexión</span>")
            self.gateway_label.setText("🚪 <b>Gateway:</b> <span style='color: #757575;'>N/A</span>")
            self.dns_label.setText("🔍 <b>DNS:</b> <span style='color: #757575;'>N/A</span>")
            self.interface_label.setText("🔌 <b>Interfaz:</b> <span style='color: #757575;'>N/A</span>")
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Estilo general de la aplicación
        self.setStyleSheet("""
            QMainWindow {
                background-color: #FAFAFA;
            }
            QWidget {
                font-family: 'Segoe UI', 'Ubuntu', 'Roboto', sans-serif;
            }
            QPushButton {
                padding: 10px 14px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 10pt;
                text-align: left;
                min-height: 36px;
                max-height: 48px;
            }
            QListWidget {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                background-color: white;
                padding: 5px;
                font-size: 10pt;
            }
            QListWidget::item {
                padding: 10px;
                border-radius: 6px;
                margin: 3px;
            }
            QListWidget::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
                border: 2px solid #2196F3;
                font-weight: bold;
            }
            QListWidget::item:hover {
                background-color: #F5F5F5;
            }
            QStatusBar {
                background-color: #E0E0E0;
                color: #424242;
                font-weight: bold;
                padding: 5px;
            }
        """)
        
        main_layout = QVBoxLayout()
        
        # Título con gradiente y estilo atractivo
        title_label = QLabel("🌐 <span style='color: #1976D2;'>NetGui</span> - Gestor de Perfiles de Red")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 16pt;
            font-weight: bold;
            padding: 12px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                        stop:0 #E3F2FD, stop:0.5 #BBDEFB, stop:1 #E3F2FD);
            border-radius: 8px;
            color: #0D47A1;
            margin-bottom: 5px;
        """)
        main_layout.addWidget(title_label)
        
        # Panel de información de red actual
        self.info_panel = self.create_info_panel()
        main_layout.addWidget(self.info_panel)
        
        # Splitter para dividir la lista y los botones
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Panel izquierdo con título y lista
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        
        # Título de la lista de perfiles
        profiles_title = QLabel("📋 Perfiles de Red Disponibles")
        profiles_title.setStyleSheet("""
            font-size: 11pt;
            font-weight: bold;
            padding: 8px;
            background-color: #E3F2FD;
            border-radius: 6px;
            color: #1976D2;
            margin-bottom: 5px;
        """)
        left_layout.addWidget(profiles_title)
        
        # Lista de perfiles
        self.profile_list = QListWidget()
        self.profile_list.itemDoubleClicked.connect(self.on_profile_double_clicked)
        self.profile_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.profile_list.customContextMenuRequested.connect(self.show_context_menu)
        left_layout.addWidget(self.profile_list)
        
        left_panel.setLayout(left_layout)
        splitter.addWidget(left_panel)
        
        # Panel de botones
        button_panel = QWidget()
        button_layout = QVBoxLayout()
        button_layout.setSpacing(6)  # Reducir espaciado entre botones
        button_layout.setContentsMargins(5, 5, 5, 5)  # Reducir márgenes
        
        # Botones de acción con estilos outline (Bootstrap-like)
        self.activate_btn = QPushButton("✅ Activar Perfil")
        self.activate_btn.clicked.connect(self.activate_profile)
        self.activate_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #4CAF50;
                border: 2px solid #4CAF50;
                font-size: 11pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                box-shadow: 0 4px 8px rgba(76, 175, 80, 0.3);
            }
            QPushButton:pressed {
                background-color: #388E3C;
                border: 2px solid #388E3C;
                box-shadow: 0 2px 4px rgba(76, 175, 80, 0.3);
            }
        """)
        button_layout.addWidget(self.activate_btn)
        
        self.duplicate_btn = QPushButton("📋 Duplicar Perfil")
        self.duplicate_btn.clicked.connect(self.duplicate_profile)
        self.duplicate_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #03A9F4;
                border: 2px solid #03A9F4;
            }
            QPushButton:hover {
                background-color: #03A9F4;
                color: white;
                border: 2px solid #03A9F4;
                box-shadow: 0 4px 8px rgba(3, 169, 244, 0.3);
            }
            QPushButton:pressed {
                background-color: #0288D1;
                border: 2px solid #0288D1;
            }
        """)
        button_layout.addWidget(self.duplicate_btn)
        
        self.edit_btn = QPushButton("✏️ Editar Perfil")
        self.edit_btn.clicked.connect(self.edit_profile)
        self.edit_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #FF9800;
                border: 2px solid #FF9800;
            }
            QPushButton:hover {
                background-color: #FF9800;
                color: white;
                border: 2px solid #FF9800;
                box-shadow: 0 4px 8px rgba(255, 152, 0, 0.3);
            }
            QPushButton:pressed {
                background-color: #F57C00;
                border: 2px solid #F57C00;
            }
        """)
        button_layout.addWidget(self.edit_btn)
        
        self.details_btn = QPushButton("ℹ️ Ver Detalles")
        self.details_btn.clicked.connect(self.show_details)
        self.details_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #9C27B0;
                border: 2px solid #9C27B0;
            }
            QPushButton:hover {
                background-color: #9C27B0;
                color: white;
                border: 2px solid #9C27B0;
                box-shadow: 0 4px 8px rgba(156, 39, 176, 0.3);
            }
            QPushButton:pressed {
                background-color: #7B1FA2;
                border: 2px solid #7B1FA2;
            }
        """)
        button_layout.addWidget(self.details_btn)
        
        self.delete_btn = QPushButton("🗑️ Eliminar Perfil")
        self.delete_btn.clicked.connect(self.delete_profile)
        self.delete_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #F44336;
                border: 2px solid #F44336;
            }
            QPushButton:hover {
                background-color: #F44336;
                color: white;
                border: 2px solid #F44336;
                box-shadow: 0 4px 8px rgba(244, 67, 54, 0.3);
            }
            QPushButton:pressed {
                background-color: #D32F2F;
                border: 2px solid #D32F2F;
                box-shadow: 0 2px 4px rgba(244, 67, 54, 0.3);
            }
        """)
        button_layout.addWidget(self.delete_btn)
        
        button_layout.addStretch()
        
        # Separador visual
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("background-color: #BDBDBD; margin: 10px 0;")
        button_layout.addWidget(separator)
        
        # Botones de gestión con estilo outline
        self.refresh_btn = QPushButton("🔄 Actualizar Lista")
        self.refresh_btn.clicked.connect(self.load_profiles)
        self.refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #607D8B;
                border: 2px solid #607D8B;
            }
            QPushButton:hover {
                background-color: #607D8B;
                color: white;
                border: 2px solid #607D8B;
                box-shadow: 0 4px 8px rgba(96, 125, 139, 0.3);
            }
            QPushButton:pressed {
                background-color: #455A64;
                border: 2px solid #455A64;
            }
        """)
        button_layout.addWidget(self.refresh_btn)
        
        self.editor_btn = QPushButton("⚙️ Editor Avanzado")
        self.editor_btn.clicked.connect(lambda: NetworkManager.open_connection_editor())
        self.editor_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #795548;
                border: 2px solid #795548;
            }
            QPushButton:hover {
                background-color: #795548;
                color: white;
                border: 2px solid #795548;
                box-shadow: 0 4px 8px rgba(121, 85, 72, 0.3);
            }
            QPushButton:pressed {
                background-color: #5D4037;
                border: 2px solid #5D4037;
            }
        """)
        button_layout.addWidget(self.editor_btn)
        
        # Separador antes de Acerca de
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.Shape.HLine)
        separator2.setFrameShadow(QFrame.Shadow.Sunken)
        separator2.setStyleSheet("background-color: #BDBDBD; margin: 10px 0;")
        button_layout.addWidget(separator2)
        
        self.about_btn = QPushButton("ℹ️ Acerca de NetGui")
        self.about_btn.clicked.connect(self.show_about)
        self.about_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #00897B;
                border: 2px solid #00897B;
            }
            QPushButton:hover {
                background-color: #00897B;
                color: white;
                border: 2px solid #00897B;
                box-shadow: 0 4px 8px rgba(0, 137, 123, 0.3);
            }
            QPushButton:pressed {
                background-color: #00695C;
                border: 2px solid #00695C;
            }
        """)
        button_layout.addWidget(self.about_btn)
        
        button_panel.setLayout(button_layout)
        button_panel.setMinimumWidth(220)  # Ancho mínimo para botones
        button_panel.setMaximumWidth(280)  # Ancho máximo para botones
        splitter.addWidget(button_panel)
        
        # Proporción: lista más ancha, botones más estrechos
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([650, 250])  # Tamaños iniciales sugeridos
        
        main_layout.addWidget(splitter)
        
        # Barra de estado
        self.statusBar().showMessage("Listo")
        
        central_widget.setLayout(main_layout)
    
    def show_context_menu(self, position):
        """Muestra menú contextual"""
        item = self.profile_list.itemAt(position)
        if not item:
            return
        
        menu = QMenu()
        menu.setStyleSheet("""
            QMenu {
                background-color: white;
                border: 2px solid #2196F3;
                border-radius: 6px;
                padding: 5px;
            }
            QMenu::item {
                padding: 8px 25px 8px 20px;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }
            QMenu::separator {
                height: 2px;
                background-color: #E0E0E0;
                margin: 5px 10px;
            }
        """)
        
        activate_action = QAction("✅ Activar", self)
        activate_action.triggered.connect(self.activate_profile)
        menu.addAction(activate_action)
        
        menu.addSeparator()
        
        duplicate_action = QAction("📋 Duplicar", self)
        duplicate_action.triggered.connect(self.duplicate_profile)
        menu.addAction(duplicate_action)
        
        edit_action = QAction("✏️ Editar", self)
        edit_action.triggered.connect(self.edit_profile)
        menu.addAction(edit_action)
        
        details_action = QAction("ℹ️ Ver Detalles", self)
        details_action.triggered.connect(self.show_details)
        menu.addAction(details_action)
        
        menu.addSeparator()
        
        delete_action = QAction("🗑️ Eliminar", self)
        delete_action.triggered.connect(self.delete_profile)
        menu.addAction(delete_action)
        
        menu.exec(self.profile_list.mapToGlobal(position))
    
    def load_profiles(self):
        """Carga la lista de perfiles de red"""
        self.statusBar().showMessage("Cargando perfiles...")
        all_profiles = NetworkManager.get_profiles()
        
        # Filtrar solo perfiles WiFi y Ethernet (excluir loopback, bridges, docker, etc.)
        self.profiles = []
        for profile in all_profiles:
            conn_type = profile.connection_type.lower()
            device = profile.device.lower() if profile.device else ""
            
            # Incluir solo WiFi y Ethernet
            if any(x in conn_type for x in ['802-11-wireless', 'wifi', 'wireless', '802-3-ethernet', 'ethernet']):
                # Excluir dispositivos virtuales comunes
                if not any(x in device for x in ['docker', 'br-', 'veth', 'lo']):
                    self.profiles.append(profile)
        
        # Guardar selección actual
        current_item = self.profile_list.currentItem()
        current_uuid = None
        if current_item:
            current_uuid = current_item.data(Qt.ItemDataRole.UserRole)
        
        self.profile_list.clear()
        
        for profile in self.profiles:
            # Iconos según el tipo de conexión
            if 'wireless' in profile.connection_type or 'wifi' in profile.connection_type.lower():
                type_icon = "📡"
            elif 'ethernet' in profile.connection_type or '802-3' in profile.connection_type:
                type_icon = "🔌"
            elif 'vpn' in profile.connection_type.lower():
                type_icon = "🔒"
            elif 'bridge' in profile.connection_type:
                type_icon = "🌉"
            elif 'loopback' in profile.connection_type:
                type_icon = "🔄"
            else:
                type_icon = "📶"
            
            status = "🟢" if profile.is_active else "⚪"
            item_text = f"{status} {type_icon} {profile.name}"
            if profile.device:
                item_text += f" · {profile.device}"
            
            item = QListWidgetItem(item_text)
            item.setData(Qt.ItemDataRole.UserRole, profile.uuid)
            
            if profile.is_active:
                item.setForeground(Qt.GlobalColor.darkGreen)
                # Hacer el texto en negrita para perfiles activos
                font = item.font()
                font.setBold(True)
                item.setFont(font)
            
            self.profile_list.addItem(item)
            
            # Restaurar selección
            if current_uuid and profile.uuid == current_uuid:
                self.profile_list.setCurrentItem(item)
        
        self.statusBar().showMessage(f"Perfiles cargados: {len(self.profiles)}", 3000)
    
    def get_selected_profile(self) -> Optional[NetworkProfile]:
        """Obtiene el perfil seleccionado"""
        current_item = self.profile_list.currentItem()
        if not current_item:
            return None
        
        uuid = current_item.data(Qt.ItemDataRole.UserRole)
        for profile in self.profiles:
            if profile.uuid == uuid:
                return profile
        
        return None
    
    def on_profile_double_clicked(self, item):
        """Maneja el doble click en un perfil"""
        self.activate_profile()
    
    def activate_profile(self):
        """Activa el perfil seleccionado"""
        profile = self.get_selected_profile()
        if not profile:
            QMessageBox.warning(self, "Error", "Por favor selecciona un perfil")
            return
        
        self.statusBar().showMessage(f"Activando perfil: {profile.name}...")
        
        # Desactivar perfil actual si es del mismo tipo
        if profile.device:
            for p in self.profiles:
                if p.is_active and p.device == profile.device:
                    NetworkManager.deactivate_profile(p.uuid)
        
        # Activar el nuevo perfil
        success, message = NetworkManager.activate_profile(profile.uuid, profile.device if profile.device else None)
        
        if success:
            QMessageBox.information(
                self, 
                "Éxito", 
                f"Perfil '{profile.name}' activado correctamente.\n\nLa interfaz se ha reiniciado automáticamente."
            )
            self.statusBar().showMessage(f"Perfil '{profile.name}' activado", 5000)
            
            # Reiniciar interfaz si tiene dispositivo asociado
            if profile.device:
                QTimer.singleShot(1000, lambda: self.restart_interface_silent(profile.device))
            
            # Actualizar información de red
            QTimer.singleShot(2500, self.update_network_info)
        else:
            QMessageBox.critical(self, "Error", f"Error al activar el perfil:\n{message}")
            self.statusBar().showMessage("Error al activar perfil", 5000)
        
        # Actualizar lista
        QTimer.singleShot(2000, self.load_profiles)
    
    def restart_interface_silent(self, interface: str):
        """Reinicia una interfaz silenciosamente"""
        NetworkManager.restart_interface(interface)
    
    def duplicate_profile(self):
        """Duplica el perfil seleccionado"""
        profile = self.get_selected_profile()
        if not profile:
            QMessageBox.warning(self, "Error", "Por favor selecciona un perfil")
            return
        
        dialog = DuplicateDialog(profile.name, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_name = dialog.new_name
            
            self.statusBar().showMessage(f"Duplicando perfil: {profile.name}...")
            success, result = NetworkManager.duplicate_profile(profile.uuid, new_name)
            
            if success:
                QMessageBox.information(
                    self, 
                    "Éxito", 
                    f"Perfil '{profile.name}' duplicado como '{new_name}'"
                )
                self.statusBar().showMessage("Perfil duplicado exitosamente", 5000)
                self.load_profiles()
            else:
                QMessageBox.critical(self, "Error", f"Error al duplicar el perfil:\n{result}")
                self.statusBar().showMessage("Error al duplicar perfil", 5000)
    
    def edit_profile(self):
        """Edita el perfil seleccionado"""
        profile = self.get_selected_profile()
        if not profile:
            QMessageBox.warning(self, "Error", "Por favor selecciona un perfil")
            return
        
        dialog = QuickEditDialog(profile, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            if dialog.settings:
                self.statusBar().showMessage(f"Modificando perfil: {profile.name}...")
                
                # Mostrar qué se va a modificar
                changes_summary = []
                for key, value in dialog.settings.items():
                    if key == 'connection.id':
                        changes_summary.append(f"Nombre → {value}")
                    elif key == 'ipv4.method':
                        method_names = {
                            'auto': 'Automático (DHCP)',
                            'manual': 'Manual (IP Fija)',
                            'link-local': 'Solo enlace local',
                            'shared': 'Compartido',
                            'disabled': 'Deshabilitado'
                        }
                        changes_summary.append(f"Método → {method_names.get(value, value)}")
                    elif key == 'ipv4.addresses':
                        changes_summary.append(f"IP → {value}")
                    elif key == 'ipv4.gateway':
                        changes_summary.append(f"Gateway → {value}")
                    elif key == 'ipv4.dns':
                        changes_summary.append(f"DNS → {value}")
                
                success, message = NetworkManager.modify_profile(profile.uuid, dialog.settings)
                
                if success:
                    changes_text = "\n".join([f"• {c}" for c in changes_summary])
                    QMessageBox.information(
                        self, 
                        "Perfil Modificado", 
                        f"El perfil '{profile.name}' se ha modificado exitosamente.\n\n"
                        f"Cambios aplicados:\n{changes_text}\n\n"
                        "Recuerda activar el perfil para que los cambios tengan efecto."
                    )
                    self.statusBar().showMessage("Perfil modificado exitosamente", 5000)
                    self.load_profiles()
                    
                    # Actualizar info de red si el perfil está activo
                    if profile.is_active:
                        QTimer.singleShot(1000, self.update_network_info)
                else:
                    QMessageBox.critical(
                        self, 
                        "Error al Modificar", 
                        f"No se pudo modificar el perfil '{profile.name}'.\n\n"
                        f"Error: {message}\n\n"
                        "Verifica que los datos sean correctos y que tengas permisos suficientes."
                    )
                    self.statusBar().showMessage("Error al modificar perfil", 5000)
            else:
                QMessageBox.information(
                    self,
                    "Sin Cambios",
                    "No se realizaron cambios en el perfil."
                )
    
    def show_details(self):
        """Muestra detalles del perfil seleccionado"""
        profile = self.get_selected_profile()
        if not profile:
            QMessageBox.warning(self, "Error", "Por favor selecciona un perfil")
            return
        
        dialog = ProfileDetailsDialog(profile, self)
        dialog.exec()
    
    def delete_profile(self):
        """Elimina el perfil seleccionado"""
        profile = self.get_selected_profile()
        if not profile:
            QMessageBox.warning(self, "Error", "Por favor selecciona un perfil")
            return
        
        reply = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que quieres eliminar el perfil '{profile.name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.statusBar().showMessage(f"Eliminando perfil: {profile.name}...")
            success, message = NetworkManager.delete_profile(profile.uuid)
            
            if success:
                QMessageBox.information(self, "Éxito", f"Perfil '{profile.name}' eliminado")
                self.statusBar().showMessage("Perfil eliminado", 5000)
                self.load_profiles()
            else:
                QMessageBox.critical(self, "Error", f"Error al eliminar el perfil:\n{message}")
                self.statusBar().showMessage("Error al eliminar perfil", 5000)
    
    def show_about(self):
        """Muestra el diálogo Acerca de"""
        dialog = AboutDialog(self)
        dialog.exec()


def main():
    """Función principal"""
    app = QApplication(sys.argv)
    app.setApplicationName("NetGui")
    app.setOrganizationName("NetGui")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

