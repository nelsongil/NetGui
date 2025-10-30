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

# Instalar icono en el tema del sistema
echo "🖼️  Instalando icono..."
ICON_SRC="media/icono.png"
ICON_DST_DIR="/usr/share/icons/hicolor/256x256/apps"
ICON_DST_PATH="$ICON_DST_DIR/netgui.png"
if [ -f "$ICON_SRC" ]; then
    mkdir -p "$ICON_DST_DIR"
    cp "$ICON_SRC" "$ICON_DST_PATH"
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

echo ""
echo "✅ ¡NetGui instalado correctamente!"
echo ""
echo "🚀 Puedes ejecutarlo de 3 formas:"
echo "   1. Desde el menú de aplicaciones: Busca 'NetGui'"
echo "   2. Desde terminal: netgui"
echo "   3. Con permisos de administrador: pkexec netgui"
echo ""
echo "📍 Ubicación: /usr/local/bin/netgui"
echo ""

