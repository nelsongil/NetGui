#!/bin/bash
# Script para instalar el ejecutable de NetGui en el sistema

set -e

# Verificar que se ejecuta como root
if [ "$EUID" -ne 0 ]; then
    echo "❌ Este script debe ejecutarse como root (sudo)"
    exit 1
fi

# Verificar que existe el ejecutable
if [ ! -f "dist/netgui" ]; then
    echo "❌ Error: No se encontró el ejecutable dist/netgui"
    echo "   Ejecuta primero: ./build_executable.sh"
    exit 1
fi

echo "📦 Instalando NetGui en el sistema..."

# Copiar ejecutable a /usr/local/bin
echo "📍 Copiando ejecutable a /usr/local/bin..."
cp dist/netgui /usr/local/bin/netgui
chmod +x /usr/local/bin/netgui

# Instalar icono en múltiples tamaños del tema del sistema
echo "🖼️  Instalando icono en múltiples tamaños..."
ICON_SRC="media/icono.png"
if [ -f "$ICON_SRC" ]; then
    # Tamaños estándar para temas de iconos
    SIZES=(16 22 24 32 48 64 128 256 512)
    
    for size in "${SIZES[@]}"; do
        DEST_DIR="/usr/share/icons/hicolor/${size}x${size}/apps"
        mkdir -p "$DEST_DIR"
        
        # Intentar redimensionar si ImageMagick está disponible
        if command -v convert &> /dev/null; then
            convert "$ICON_SRC" -resize "${size}x${size}" "$DEST_DIR/netgui.png" 2>/dev/null || \
            cp "$ICON_SRC" "$DEST_DIR/netgui.png"
        elif command -v magick &> /dev/null; then
            magick "$ICON_SRC" -resize "${size}x${size}" "$DEST_DIR/netgui.png" 2>/dev/null || \
            cp "$ICON_SRC" "$DEST_DIR/netgui.png"
        else
            # Si no hay ImageMagick, copiar el original (el sistema lo escalará)
            cp "$ICON_SRC" "$DEST_DIR/netgui.png"
        fi
    done
    
    # También en scalable
    mkdir -p "/usr/share/icons/hicolor/scalable/apps"
    cp "$ICON_SRC" "/usr/share/icons/hicolor/scalable/apps/netgui.png"
    
    echo "  ✓ Iconos instalados en todos los tamaños"
else
    echo "⚠️  Advertencia: No se encontró $ICON_SRC. Se usará el icono por defecto del sistema."
fi

# Crear archivo .desktop para el menú de aplicaciones
echo "🖥️  Creando entrada en el menú de aplicaciones..."
cat > /usr/share/applications/netgui.desktop << 'EOF'
[Desktop Entry]
Version=1.3.0
Type=Application
Name=NetGui
GenericName=Network Profile Manager
Comment=Gestor moderno de perfiles de red
Exec=pkexec /usr/local/bin/netgui
Icon=netgui
Terminal=false
Categories=System;Settings;Network;
Keywords=network;wifi;ethernet;connection;profile;manager;
StartupNotify=true
EOF

# Actualizar base de datos de aplicaciones
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database /usr/share/applications
fi

# Actualizar la caché de iconos si corresponde
if command -v gtk-update-icon-cache &> /dev/null; then
    if [ -d "/usr/share/icons/hicolor" ]; then
        gtk-update-icon-cache -f /usr/share/icons/hicolor || true
    fi
fi

# Refrescar cachés de KDE/Plasma si está disponible
if command -v kbuildsycoca6 &> /dev/null; then
    kbuildsycoca6 --noincremental || true
fi

# Obtener el usuario real (no root) para crear acceso directo en su escritorio
REAL_USER=${SUDO_USER:-$USER}
REAL_HOME=$(eval echo ~$REAL_USER)
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Crear acceso directo en el escritorio del usuario
echo "📱 Creando acceso directo en el escritorio..."
DESKTOP_DIR="$REAL_HOME/Escritorio"
# Fallback si Escritorio no existe, usar Desktop
if [ ! -d "$DESKTOP_DIR" ]; then
    DESKTOP_DIR="$REAL_HOME/Desktop"
fi

mkdir -p "$DESKTOP_DIR"

# Ruta absoluta al icono del proyecto
ICON_PATH="$PROJECT_DIR/media/icono.png"

# Si el icono existe en el proyecto, usar esa ruta
if [ -f "$ICON_PATH" ]; then
    # Crear archivo temporal con el contenido .desktop
    TMP_DESKTOP=$(mktemp)
    cat > "$TMP_DESKTOP" << EOF
[Desktop Entry]
Version=1.3.0
Type=Application
Name=NetGui
GenericName=Network Profile Manager
Comment=Gestor moderno de perfiles de red
Exec=/usr/local/bin/netgui
Icon=$ICON_PATH
Terminal=false
Categories=System;Settings;Network;
Keywords=network;wifi;ethernet;connection;profile;manager;
StartupNotify=true
EOF
    # Copiar al escritorio del usuario
    cp "$TMP_DESKTOP" "$DESKTOP_DIR/NetGui.desktop"
    chown "$REAL_USER:$REAL_USER" "$DESKTOP_DIR/NetGui.desktop"
    chmod +x "$DESKTOP_DIR/NetGui.desktop"
    rm -f "$TMP_DESKTOP"
    echo "  ✓ Acceso directo creado en: $DESKTOP_DIR/NetGui.desktop"
else
    echo "  ⚠️  Advertencia: No se encontró el icono en $ICON_PATH"
fi

# También crear en aplicaciones locales del usuario
LOCAL_APPS_DIR="$REAL_HOME/.local/share/applications"
mkdir -p "$LOCAL_APPS_DIR"

if [ -f "$ICON_PATH" ]; then
    TMP_DESKTOP=$(mktemp)
    cat > "$TMP_DESKTOP" << EOF
[Desktop Entry]
Version=1.3.0
Type=Application
Name=NetGui
GenericName=Network Profile Manager
Comment=Gestor moderno de perfiles de red
Exec=/usr/local/bin/netgui
Icon=$ICON_PATH
Terminal=false
Categories=System;Settings;Network;
Keywords=network;wifi;ethernet;connection;profile;manager;
StartupNotify=true
EOF
    cp "$TMP_DESKTOP" "$LOCAL_APPS_DIR/netgui.desktop"
    chown "$REAL_USER:$REAL_USER" "$LOCAL_APPS_DIR/netgui.desktop"
    chmod +x "$LOCAL_APPS_DIR/netgui.desktop"
    rm -f "$TMP_DESKTOP"
    
    # Actualizar caché de aplicaciones del usuario
    if command -v update-desktop-database &> /dev/null; then
        sudo -u "$REAL_USER" update-desktop-database "$LOCAL_APPS_DIR" 2>/dev/null || true
    fi
fi

echo ""
echo "✅ ¡NetGui instalado correctamente!"
echo ""
echo "🚀 Puedes ejecutarlo de 4 formas:"
echo "   1. Desde el escritorio: Doble click en 'NetGui.desktop'"
echo "   2. Desde el menú de aplicaciones: Busca 'NetGui'"
echo "   3. Desde terminal: netgui"
echo "   4. Con permisos de administrador: pkexec netgui"
echo ""
echo "📍 Ubicación ejecutable: /usr/local/bin/netgui"
echo "📍 Acceso directo: $DESKTOP_DIR/NetGui.desktop"
echo ""

