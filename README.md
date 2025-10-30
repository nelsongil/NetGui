# 🌐 NetGui - Gestor de Perfiles de Red

**Versión 1.3.0** - Aplicación moderna para gestionar perfiles de red en Debian 13 con KDE Plasma

![NetGui](https://img.shields.io/badge/KDE-Plasma-blue)
![Python](https://img.shields.io/badge/Python-3.11+-green)
![Version](https://img.shields.io/badge/Version-1.3.0-orange)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)

---

## 🚀 Inicio Rápido

### Instalación Automática (Recomendada)

```bash
cd /home/nelson/MEGAsync/desarrollo/NetGui
sudo ./install.sh
netgui
```

### Ejecución Directa

```bash
# Instalar dependencias
sudo apt install network-manager python3 python3-pip python3-venv network-manager-gnome

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Ejecutar
python3 main.py
```

### Generar Ejecutable

Si prefieres un ejecutable standalone:

```bash
# Generar ejecutable
./build_executable.sh

# Ejecutar directamente
./dist/netgui

# Instalar en el sistema (opcional)
sudo ./install_executable.sh
```

El ejecutable se instalará en `/usr/local/bin/netgui` y aparecerá en tu menú de aplicaciones.

---

## ✨ Características Principales

- 🔌 **Perfil activo visible** en negrita en panel de información
- 🌐 **Monitor de red** en tiempo real (IP, Gateway, DNS, Interfaz)
- 🔄 **Cambio rápido** entre perfiles con un click
- 📋 **Duplicar y editar** perfiles fácilmente
- ✅ **Validación completa** de IPs, Gateway y DNS
- 🎨 **Interfaz moderna** con Material Design
- 🔌 **Solo WiFi y Ethernet** (filtra bridges, docker, etc.)
- ℹ️ **Acerca de** con información de la aplicación

---

## 📚 Documentación Completa

Toda la documentación está organizada en la carpeta **`documentacion/`**:

- **[README](documentacion/README.md)** - Guía completa del proyecto
- **[QUICK_START](documentacion/QUICK_START.md)** - Inicio rápido paso a paso
- **[INTERFACE_GUIDE](documentacion/INTERFACE_GUIDE.md)** - Guía detallada de la interfaz
- **[VISUAL_GUIDE](documentacion/VISUAL_GUIDE.md)** - Guía de diseño visual
- **[VALIDACION](documentacion/VALIDACION.md)** - Validación de datos
- **[TEST_GUIDE](documentacion/TEST_GUIDE.md)** - Guía de pruebas
- **[CHANGELOG](documentacion/CHANGELOG.md)** - Historial de cambios
- **[RESUMEN](documentacion/RESUMEN.md)** - Resumen del proyecto

---

## 🎯 Casos de Uso

### Red en Casa vs Trabajo
```
1. Duplicar perfil actual → "Casa - DHCP"
2. Duplicar perfil actual → "Trabajo - IP Fija 192.168.1.50"
3. Cambiar entre perfiles con doble click
```

### Diferentes DNS
```
1. Perfil: "Internet - DNS Google" (8.8.8.8)
2. Perfil: "Internet - DNS Cloudflare" (1.1.1.1)
3. Cambio rápido para probar velocidad
```

---

## 🛠️ Tecnología

- **Backend**: NetworkManager (nmcli)
- **Frontend**: PyQt6
- **Sistema**: Debian 13 (Trixie) / KDE Plasma 6
- **Python**: 3.11+

---

## 📄 Licencia

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**

Este proyecto es código abierto para uso **personal, educativo y no comercial**.

✅ Puedes:
- Usar libremente para proyectos personales
- Estudiar y aprender del código
- Modificar y adaptar
- Compartir con otros (con atribución)

❌ No puedes:
- Usar comercialmente
- Vender el software o servicios basados en él

Para más detalles, ver [LICENSE](LICENSE)

💼 **Uso Comercial:** Si deseas usar NetGui comercialmente, contacta al autor.

---

## 🆘 Soporte

Para más información consulta la [documentación completa](documentacion/) o ejecuta:

```bash
python3 check_dependencies.py  # Verificar dependencias
```

---

**Desarrollado con ❤️ para la comunidad Linux**
