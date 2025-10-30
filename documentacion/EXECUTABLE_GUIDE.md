# Guía del Ejecutable NetGui

Esta guía explica cómo generar, instalar y distribuir el ejecutable standalone de NetGui.

## 📦 ¿Qué es el Ejecutable Standalone?

El ejecutable standalone es una versión compilada de NetGui que **incluye todas las dependencias** (Python, PyQt6, etc.) en un solo archivo. Esto significa:

✅ **No necesitas Python instalado**  
✅ **No necesitas crear entorno virtual**  
✅ **No necesitas instalar dependencias con pip**  
✅ **Más rápido que ejecutar scripts Python**  
✅ **Fácil de distribuir y compartir**

## 🔨 Generar el Ejecutable

### Opción 1: Script Automatizado (Recomendado)

```bash
cd /home/nelson/MEGAsync/desarrollo/NetGui
./build_executable.sh
```

El script:
1. Verifica que exista el entorno virtual
2. Instala PyInstaller si no está instalado
3. Limpia compilaciones anteriores
4. Genera el ejecutable en `dist/netgui`
5. Muestra el tamaño final

### Opción 2: Manual

```bash
# Activar entorno virtual
source venv/bin/activate

# Instalar PyInstaller
pip install pyinstaller

# Generar ejecutable
pyinstaller --clean netgui.spec
```

## 📊 Detalles Técnicos

### Tamaño y Formato

- **Tamaño**: ~57 MB
- **Formato**: ELF 64-bit executable
- **Arquitectura**: x86-64
- **Sistema**: GNU/Linux 3.2.0+

### Contenido Incluido

El ejecutable contiene:
- Python 3.13 runtime
- PyQt6 y todas sus dependencias
- NetworkManager bindings
- Todos los módulos de NetGui
- Recursos estáticos (LICENSE, README, etc.)

### Optimizaciones

- **UPX**: Compresión activada para reducir tamaño
- **Strip**: Símbolos de debug eliminados
- **One-file**: Todo empaquetado en un solo archivo

## 🚀 Instalar en el Sistema

### Instalación Automática

```bash
sudo ./install_executable.sh
```

El script de instalación:
1. Copia el ejecutable a `/usr/local/bin/netgui`
2. Le da permisos de ejecución
3. Crea un archivo `.desktop` en `/usr/share/applications/`
4. Actualiza la base de datos de aplicaciones

### Instalación Manual

```bash
# Copiar ejecutable
sudo cp dist/netgui /usr/local/bin/netgui
sudo chmod +x /usr/local/bin/netgui

# Crear entrada en el menú
sudo nano /usr/share/applications/netgui.desktop
```

Contenido del archivo `.desktop`:

```ini
[Desktop Entry]
Version=1.3.0
Type=Application
Name=NetGui
GenericName=Network Profile Manager
Comment=Gestor moderno de perfiles de red
Exec=pkexec /usr/local/bin/netgui
Icon=network-workgroup
Terminal=false
Categories=System;Settings;Network;
Keywords=network;wifi;ethernet;connection;profile;manager;
StartupNotify=true
```

## 🎯 Uso del Ejecutable

### Opción 1: Desde el Menú de Aplicaciones

1. Abre el lanzador de aplicaciones de KDE
2. Busca "NetGui"
3. Haz click para ejecutar

### Opción 2: Desde Terminal

```bash
# Ejecutar localmente (sin instalar)
./dist/netgui

# Ejecutar después de instalar
netgui

# Con permisos de administrador
pkexec netgui
```

## 📤 Distribuir el Ejecutable

### Compartir con Otros Usuarios

El ejecutable es **completamente portable**. Puedes:

1. **Copiar directamente**: 
   ```bash
   cp dist/netgui /ruta/destino/
   chmod +x /ruta/destino/netgui
   ```

2. **Comprimir para compartir**:
   ```bash
   tar -czf netgui-1.3.0-linux-x64.tar.gz -C dist netgui
   ```

3. **Crear paquete DEB** (avanzado):
   - Crear estructura de paquete Debian
   - Incluir el ejecutable y el .desktop
   - Usar `dpkg-deb` para generar .deb

### Requisitos del Sistema Receptor

El sistema donde se ejecute el ejecutable necesita:
- ✅ Debian 13 (Trixie) o compatible
- ✅ NetworkManager instalado
- ✅ Sistema de ventanas X11/Wayland
- ❌ **NO** necesita Python
- ❌ **NO** necesita PyQt6
- ❌ **NO** necesita pip/venv

## 🔧 Troubleshooting

### Error: "No se puede conectar al display"

```bash
# Verificar que DISPLAY está configurado
echo $DISPLAY

# Si está vacío, configurarlo
export DISPLAY=:0
```

### Error: "Permiso denegado"

```bash
# Dar permisos de ejecución
chmod +x dist/netgui
```

### El ejecutable es muy grande

El tamaño de ~57MB es normal para aplicaciones PyQt6 porque incluye:
- Runtime de Python (~15MB)
- Librerías Qt6 (~30MB)
- Dependencias del sistema (~12MB)

Para reducir tamaño (no recomendado):
- Deshabilitar UPX
- Excluir módulos no usados
- Crear ejecutable "dir" en lugar de "one-file"

### Warning sobre libtiff.so.5

Este warning durante la compilación es **normal** y **no afecta** la funcionalidad de NetGui. Es una dependencia opcional de Qt6 para formatos de imagen TIFF.

## 🆚 Comparación: Script vs Ejecutable

| Característica | Script Python | Ejecutable |
|---------------|---------------|------------|
| **Tamaño** | ~50 KB | ~57 MB |
| **Requiere Python** | ✅ Sí | ❌ No |
| **Requiere venv** | ✅ Sí | ❌ No |
| **Velocidad inicio** | ~2-3 seg | ~1 seg |
| **Facilidad distribución** | ⚠️ Compleja | ✅ Simple |
| **Portabilidad** | ⚠️ Media | ✅ Alta |
| **Actualización código** | ✅ Inmediata | ⚠️ Recompilar |
| **Debug** | ✅ Fácil | ⚠️ Limitado |

## 📝 Recomendaciones

### Para Desarrollo
- Usar el script Python (`python3 main.py`)
- Más rápido para hacer cambios
- Mejor debugging
- No necesita recompilar

### Para Producción/Distribución
- Usar el ejecutable
- Mejor experiencia de usuario
- No requiere dependencias
- Más profesional

### Para Testing
- Probar ambas versiones
- Verificar que el ejecutable funciona igual
- Comprobar permisos de red

## 🔄 Actualizar el Ejecutable

Cuando hagas cambios en el código:

```bash
# 1. Hacer cambios en main.py, network_manager.py, etc.

# 2. Probar con script
python3 main.py

# 3. Si todo funciona, recompilar
./build_executable.sh

# 4. Probar ejecutable
./dist/netgui

# 5. Si todo está OK, reinstalar
sudo ./install_executable.sh
```

## 🎯 Próximos Pasos

### Crear Paquete .deb

Para una distribución más profesional, considera crear un paquete Debian:

1. Estructura del paquete
2. Scripts de post-instalación
3. Integración con apt
4. Firma del paquete

### Crear AppImage

Para máxima portabilidad en todas las distribuciones Linux:

1. Usar `appimage-builder`
2. Empaquetar con todas las dependencias
3. Funciona en cualquier distro
4. Auto-actualización integrada

## 📞 Soporte

Si tienes problemas con el ejecutable:

1. Verifica que `dist/netgui` existe
2. Comprueba permisos de ejecución
3. Ejecuta en terminal para ver errores
4. Verifica dependencias del sistema
5. Consulta la [documentación principal](README.md)

---

**Última actualización**: v1.3.0 - 2025-10-30

