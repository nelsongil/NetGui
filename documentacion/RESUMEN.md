# NetGui - Resumen del Proyecto

## 🎯 Objetivo

NetGui es una aplicación gráfica para **Debian 13 (Trixie)** con **KDE Plasma** que permite gestionar perfiles de red de manera sencilla. Está diseñada como interfaz gráfica moderna sobre NetworkManager, usando `nm-connection-editor` como base para edición avanzada.

## ✨ Características Implementadas

### 🌐 Monitor de Red en Tiempo Real
- Visualización de IP actual, Gateway, DNS e Interfaz
- Actualización automática cada 3 segundos
- Soporte para múltiples interfaces simultáneas
- Priorización inteligente (Ethernet sobre WiFi)
- Texto seleccionable para copiar fácilmente

### 🔄 Gestión de Perfiles
- **Listar**: Todos los perfiles con indicador visual de estado (● activo / ○ inactivo)
- **Activar**: Con un solo click o doble click + reinicio automático de interfaz
- **Duplicar**: Crear copias de perfiles para variantes (ej: DHCP vs IP fija)
- **Editar**: Editor rápido para parámetros comunes + integración con nm-connection-editor
- **Eliminar**: Con confirmación de seguridad
- **Ver Detalles**: Visualización completa de toda la configuración

### 🖥️ Interfaz de Usuario
- Diseño moderno con PyQt6 optimizado para KDE Plasma
- Actualización automática (perfiles cada 5s, red cada 3s)
- Menú contextual (click derecho) para acceso rápido
- Tooltips informativos
- Barra de estado con feedback de operaciones
- Panel separado para acciones

### 🔧 Integración con Sistema
- Usa NetworkManager (nmcli) como backend
- Integración con nm-connection-editor para edición avanzada
- Archivo .desktop para menú de aplicaciones KDE
- Script de instalación automática
- Comando global opcional (`netgui`)

## 📁 Estructura del Proyecto

```
NetGui/
├── main.py                    # Aplicación principal con interfaz Qt6
├── network_manager.py         # Módulo de gestión de NetworkManager
├── requirements.txt           # Dependencias Python (PyQt6)
├── install.sh                 # Script de instalación automática
├── check_dependencies.py      # Verificador de dependencias
├── netgui.desktop            # Integración con KDE
├── .gitignore                # Archivos a ignorar en git
│
├── README.md                 # Documentación completa
├── QUICK_START.md            # Guía de inicio rápido
├── INTERFACE_GUIDE.md        # Guía detallada de la interfaz
├── TEST_GUIDE.md             # Guía de pruebas
├── CHANGELOG.md              # Historial de cambios
├── LICENSE                   # Licencia MIT
└── RESUMEN.md               # Este archivo
```

## 🚀 Instalación Rápida

### Opción 1: Instalación Automática (Recomendada)

```bash
cd /home/nelson/MEGAsync/desarrollo/NetGui
sudo ./install.sh
netgui
```

### Opción 2: Instalación Manual

```bash
# Instalar dependencias del sistema
sudo apt install network-manager python3 python3-pip python3-venv network-manager-gnome

# Crear entorno virtual
cd /home/nelson/MEGAsync/desarrollo/NetGui
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
pip install -r requirements.txt

# Ejecutar
python3 main.py
```

## 📖 Documentación

| Archivo | Propósito | Para quién |
|---------|-----------|------------|
| `README.md` | Documentación completa del proyecto | Todos |
| `QUICK_START.md` | Guía rápida de inicio | Usuarios nuevos |
| `INTERFACE_GUIDE.md` | Explicación detallada de la interfaz | Usuarios |
| `TEST_GUIDE.md` | Guía de pruebas y verificación | Desarrolladores/Testers |
| `CHANGELOG.md` | Historial de versiones y cambios | Todos |
| `RESUMEN.md` | Visión general del proyecto | Evaluadores/Nuevos usuarios |

## 💻 Requisitos del Sistema

- **OS**: Debian 13 (Trixie) o superior
- **DE**: KDE Plasma 6
- **Python**: 3.11+
- **Sistema**:
  - NetworkManager (activo)
  - nm-connection-editor
  - python3-venv
  - python3-pip

## 🎨 Interfaz de Usuario

### Vista Principal

```
┌─────────────────────────────────────────────────┐
│          NetGui - Gestor de Perfiles            │
├─────────────────────────────────────────────────┤
│ [Panel Info Red]                                │
│  IP: 192.168.1.100/24                          │
│  Gateway: 192.168.1.1                          │
│  DNS: 8.8.8.8, 8.8.4.4                         │
│  Interfaz: enp0s3 (ethernet) - connected       │
├──────────────────────────┬──────────────────────┤
│ ● Red Casa (ethernet)    │  ✓ Activar Perfil   │
│   - enp0s3              │  ⎘ Duplicar Perfil  │
│ ○ Red Trabajo           │  ✎ Editar Perfil    │
│   - enp0s3              │  ⓘ Ver Detalles     │
│ ○ WiFi Casa             │  🗑 Eliminar         │
│   - wlan0               │  ↻ Actualizar        │
│                         │  ⚙ Editor Avanzado   │
└──────────────────────────┴──────────────────────┘
```

## 🔑 Funcionalidades Clave

### 1. Cambio de Perfil con un Click
```python
# Usuario hace doble click en perfil
# → NetGui desactiva perfil anterior
# → Activa nuevo perfil
# → Reinicia interfaz automáticamente
# → Actualiza información de red
# → Muestra confirmación
```

### 2. Duplicación de Perfiles
```python
# Usuario selecciona perfil "Red Casa"
# → Click en "Duplicar"
# → Ingresa nombre: "Red Casa - IP Fija"
# → NetGui crea copia exacta
# → Usuario puede editarla sin afectar original
```

### 3. Monitor de Red en Tiempo Real
```python
# Cada 3 segundos:
# → Lee información de NetworkManager
# → Actualiza IP, Gateway, DNS, Interfaz
# → Prioriza Ethernet sobre WiFi
# → Muestra tooltip con múltiples interfaces
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: NetworkManager (nmcli)
- **Frontend**: PyQt6
- **Lenguaje**: Python 3.11+
- **Sistema**: Linux (Debian 13)
- **DE**: KDE Plasma 6

## 📊 Casos de Uso

### Caso 1: Usuario con Laptop
```
Escenario: Usuario con diferentes redes en casa y trabajo

Solución:
1. Duplica perfil actual → "Casa - DHCP"
2. Duplica perfil actual → "Trabajo - IP Fija 192.168.1.50"
3. Duplica perfil actual → "Trabajo - IP Fija 192.168.1.51"

Uso:
- En casa: Doble click en "Casa - DHCP"
- En trabajo (PC 1): Doble click en "Trabajo - IP Fija .50"
- En trabajo (PC 2): Doble click en "Trabajo - IP Fija .51"
```

### Caso 2: Servidor con Múltiples Configuraciones
```
Escenario: Servidor que necesita diferentes IPs según servicio

Solución:
1. "Servidor - Web (IP .100)"
2. "Servidor - DB (IP .101)"
3. "Servidor - Desarrollo (DHCP)"

Uso: Cambio rápido según necesidad del momento
```

### Caso 3: Testing de Red
```
Escenario: Necesidad de probar diferentes DNS

Solución:
1. "Red - DNS Google (8.8.8.8)"
2. "Red - DNS Cloudflare (1.1.1.1)"
3. "Red - DNS ISP (automático)"

Uso: Cambio rápido para comparar velocidad/funcionalidad
```

## 🔒 Seguridad

- ✅ No almacena contraseñas
- ✅ Usa permisos del sistema (NetworkManager)
- ✅ Confirmación antes de eliminar perfiles
- ✅ No ejecuta comandos arbitrarios
- ✅ Operaciones solo sobre NetworkManager

## 🐛 Testing y Calidad

- ✅ Sin errores de linting (Python)
- ✅ Manejo de errores robusto
- ✅ Actualización sin bloqueos
- ✅ Verificador de dependencias incluido
- ✅ Guía completa de pruebas (TEST_GUIDE.md)

## 📈 Métricas del Código

```
Archivos principales:
- main.py: ~600 líneas
- network_manager.py: ~270 líneas
Total funcional: ~870 líneas de Python

Documentación:
- README.md: Completo
- QUICK_START.md: Guía básica
- INTERFACE_GUIDE.md: Guía detallada
- TEST_GUIDE.md: Guía de pruebas
- CHANGELOG.md: Versiones
Total documentación: ~1000+ líneas

Scripts:
- install.sh: Instalación automática
- check_dependencies.py: Verificación
```

## 🎯 Objetivos Cumplidos

✅ **Seleccionar perfiles**: Lista completa con estado visual  
✅ **Duplicar perfiles**: Funcionalidad completa con nombrado  
✅ **Modificar perfiles**: Editor rápido + integración nm-connection-editor  
✅ **Cambio con un click**: Doble click o botón activa inmediatamente  
✅ **Reinicio automático**: Interfaz se reinicia tras cambio de perfil  
✅ **Visualización de IP**: Panel en tiempo real con toda la info  
✅ **Base en nm-connection-editor**: Integración completa  
✅ **KDE Plasma**: Optimizado con PyQt6  
✅ **Debian 13**: Probado y compatible  

## 🚀 Próximos Pasos (Roadmap)

### Versión 1.1 (Planificada)
- Soporte IPv6
- Gestión de VPN
- Perfiles favoritos
- Import/Export de perfiles
- Notificaciones del sistema

### Versión 1.2 (Planificada)
- Systray indicator
- Atajos de teclado
- Backup automático
- Estadísticas de uso
- Medidor de velocidad

## 📝 Notas Finales

### Para Usuarios
- La aplicación está **lista para uso en producción**
- Sigue `QUICK_START.md` para comenzar rápidamente
- Usa `TEST_GUIDE.md` si encuentras problemas

### Para Desarrolladores
- El código está bien documentado
- Sigue estándares de Python (PEP 8)
- Usa NetworkManager API de forma segura
- Fácil de extender con nuevas funcionalidades

### Para Administradores
- Instalación simple con script automático
- Se integra con permisos existentes de NetworkManager
- No requiere configuración adicional del sistema
- Compatible con Polkit para seguridad

## 📞 Soporte

Para problemas o preguntas:
1. Consulta `README.md` para documentación completa
2. Revisa `TEST_GUIDE.md` para solución de problemas
3. Ejecuta `python3 check_dependencies.py` para verificar sistema
4. Revisa logs: `journalctl -u NetworkManager`

## 📜 Licencia

MIT License - Ver archivo `LICENSE` para detalles completos.

---

**NetGui v1.0.0** - Octubre 2025  
Gestor de Perfiles de Red para Debian 13 (Trixie) con KDE Plasma

Creado con ❤️ para facilitar la gestión de redes en Linux

