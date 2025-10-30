#!/bin/bash
# Script para generar el ejecutable de NetGui

set -e

echo "🔨 Generando ejecutable de NetGui..."

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Error: No se encontró el entorno virtual 'venv'"
    echo "   Ejecuta primero: python3 -m venv venv && source venv/bin/activate"
    exit 1
fi

# Verificar que PyInstaller está instalado
if ! command -v pyinstaller &> /dev/null; then
    echo "📦 Instalando PyInstaller..."
    pip install pyinstaller
fi

# Limpiar builds anteriores
echo "🧹 Limpiando builds anteriores..."
rm -rf build dist

# Generar ejecutable
echo "⚙️  Compilando con PyInstaller..."
pyinstaller --clean netgui.spec

# Verificar que se generó correctamente
if [ -f "dist/netgui" ]; then
    SIZE=$(du -h dist/netgui | cut -f1)
    echo ""
    echo "✅ ¡Ejecutable generado exitosamente!"
    echo "   📍 Ubicación: dist/netgui"
    echo "   📊 Tamaño: $SIZE"
    echo ""
    echo "🚀 Para ejecutar:"
    echo "   ./dist/netgui"
    echo ""
    echo "💾 Para instalar en el sistema:"
    echo "   sudo ./install_executable.sh"
else
    echo "❌ Error: No se pudo generar el ejecutable"
    exit 1
fi

