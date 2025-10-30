# NetGui - Gestor Gráfico de Perfiles de Red

![NetGui](https://img.shields.io/badge/KDE-Plasma-blue)
![Python](https://img.shields.io/badge/Python-3.11+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Aplicación gráfica para gestionar perfiles de red en Debian 13 (Trixie) con KDE Plasma, utilizando NetworkManager como backend.

## Características

✨ **Funcionalidades principales:**

- 🌐 **Monitor de red en tiempo real**: Visualiza tu IP actual, gateway, DNS e interfaz activa
- 🔍 **Visualización de perfiles**: Lista todos tus perfiles de red con indicador de estado (activo/inactivo)
- 🔄 **Cambio rápido**: Activa cualquier perfil con un solo click
- 📋 **Duplicación**: Duplica perfiles existentes para crear variantes rápidamente
- ✏️ **Edición rápida**: Modifica parámetros comunes (IP, gateway, DNS) directamente
- ⚙️ **Edición avanzada**: Integración con `nm-connection-editor` para configuración completa
- 🔃 **Reinicio automático**: Las interfaces se reinician automáticamente al cambiar perfiles
- 📊 **Detalles completos**: Visualiza toda la configuración de cualquier perfil
- 🗑️ **Gestión completa**: Elimina perfiles que ya no necesites
- 🔄 **Actualización automática**: La lista y la información de red se actualizan automáticamente

## Requisitos del Sistema

- **Sistema Operativo**: Debian 13 (Trixie) o superior
- **Entorno de Escritorio**: KDE Plasma 6
- **Python**: 3.11 o superior
- **NetworkManager**: Debe estar instalado y activo
- **Paquetes del sistema**:
  - `network-manager`
  - `python3`
  - `python3-pip`
  - `python3-venv`

## Instalación

### 1. Instalar dependencias del sistema

```bash
sudo apt update
sudo apt install network-manager python3 python3-pip python3-venv
```

### 2. Crear entorno virtual e instalar dependencias Python

```bash
cd /home/nelson/MEGAsync/desarrollo/NetGui
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Hacer ejecutable el script principal

```bash
chmod +x main.py
chmod +x network_manager.py
```

### 4. (Opcional) Instalación global

Para usar la aplicación desde cualquier lugar, puedes crear un script de lanzamiento:

```bash
# Crear script de lanzamiento
sudo bash -c 'cat > /usr/local/bin/netgui << EOF
#!/bin/bash
cd /home/nelson/MEGAsync/desarrollo/NetGui
source venv/bin/activate
python3 main.py "\$@"
EOF'

sudo chmod +x /usr/local/bin/netgui
```

### 5. (Opcional) Integración con KDE

Instalar archivo `.desktop` para acceder desde el menú de aplicaciones:

```bash
sudo cp netgui.desktop /usr/share/applications/
sudo update-desktop-database
```

## Uso

### Ejecutar la aplicación

```bash
# Si instalaste globalmente
netgui

# O directamente desde el directorio del proyecto
cd /home/nelson/MEGAsync/desarrollo/NetGui
source venv/bin/activate
python3 main.py
```

### Interfaz de la aplicación

La aplicación muestra:

1. **Panel de Información de Red**: En la parte superior, muestra en tiempo real:
   - **🔌 Nombre del perfil activo** (en negrita y destacado en azul)
   - 🌐 **Dirección IP** actual (verde)
   - 🚪 **Puerta de enlace** (Gateway) (azul)
   - 🔍 **Servidores DNS** configurados (morado)
   - 🔌/📡 **Interfaz** de red activa y su estado (naranja)
   - Si tienes múltiples interfaces activas, puedes pasar el cursor sobre la IP para ver todas
   - Panel con borde verde y fondo gris claro para mejor visibilidad

2. **Lista de Perfiles**: Muestra todos los perfiles de red disponibles:
   - 🟢 indica perfil activo (texto en **negrita** y verde)
   - ⚪ indica perfil inactivo
   - Iconos según tipo: 📡 WiFi, 🔌 Ethernet, 🔒 VPN, 🌉 Bridge, 🔄 Loopback
   - Muestra tipo de conexión y dispositivo asociado
   - Efectos visuales al pasar el mouse y seleccionar

3. **Botones de Acción**: Panel lateral con todas las operaciones disponibles

### Operaciones principales

1. **Activar un perfil**:
   - Selecciona el perfil deseado en la lista
   - Haz doble click o presiona el botón "Activar Perfil"
   - La interfaz se reiniciará automáticamente

2. **Duplicar un perfil**:
   - Selecciona el perfil que deseas duplicar
   - Click en "Duplicar Perfil"
   - Ingresa el nombre para el nuevo perfil
   - El perfil duplicado aparecerá en la lista

3. **Editar un perfil**:
   - **Edición rápida**: Click en "Editar Perfil" para cambiar parámetros comunes
     - Selecciona el método IPv4 del dropdown (Automático/DHCP o Manual/IP Fija)
     - Modifica IP, Gateway y DNS según necesites
   - **Edición avanzada**: Usa el botón "Editor Avanzado" dentro del diálogo o el botón principal "Abrir nm-connection-editor"

4. **Ver detalles**:
   - Selecciona un perfil y click en "Ver Detalles"
   - Se mostrará toda la configuración del perfil

5. **Eliminar un perfil**:
   - Selecciona el perfil a eliminar
   - Click en "Eliminar Perfil"
   - Confirma la eliminación

### Menú contextual

También puedes hacer click derecho sobre cualquier perfil para acceder rápidamente a todas las opciones.

## Permisos

Para reiniciar interfaces de red sin solicitar contraseña cada vez, puedes configurar `sudo` (opcional):

```bash
sudo visudo
```

Agrega al final (reemplaza `tu_usuario` con tu nombre de usuario):

```
tu_usuario ALL=(ALL) NOPASSWD: /usr/bin/nmcli
```

**Nota de seguridad**: Esta configuración permite ejecutar `nmcli` sin contraseña. Evalúa los riesgos de seguridad según tu entorno.

## Estructura del Proyecto

```
NetGui/
├── main.py                 # Aplicación principal con interfaz Qt
├── network_manager.py      # Módulo de gestión de NetworkManager
├── requirements.txt        # Dependencias Python
├── README.md              # Este archivo
├── netgui.desktop         # Archivo de integración con KDE
└── venv/                  # Entorno virtual (creado durante instalación)
```

## Solución de Problemas

### La aplicación no inicia

1. Verifica que NetworkManager esté activo:
```bash
systemctl status NetworkManager
```

2. Asegúrate de que el entorno virtual esté activado:
```bash
source venv/bin/activate
```

3. Verifica las dependencias:
```bash
pip list | grep PyQt6
```

### No se pueden modificar/activar perfiles

1. Verifica que tienes permisos adecuados para gestionar redes
2. Intenta ejecutar `nmcli` manualmente para verificar acceso:
```bash
nmcli connection show
```

### El editor avanzado no abre

Instala `nm-connection-editor` si no está presente:
```bash
sudo apt install network-manager-gnome
```

## Compatibilidad

- ✅ Debian 13 (Trixie)
- ✅ KDE Plasma 6
- ✅ Python 3.11+
- ✅ NetworkManager 1.40+

Debería funcionar en otras distribuciones basadas en Debian/Ubuntu con ajustes menores.

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## Autor

Creado para Debian 13 (Trixie) con KDE Plasma 6

## Agradecimientos

- NetworkManager por la gestión de redes
- PyQt6 por el framework de interfaz gráfica
- KDE Plasma por el entorno de escritorio

