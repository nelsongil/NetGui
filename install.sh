#!/bin/bash
# Script de instalación para NetGui

set -e

echo "======================================"
echo "   NetGui - Script de Instalación"
echo "======================================"
echo ""

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Verificar si se ejecuta como root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}Este script debe ejecutarse con privilegios de root (sudo)${NC}"
    exit 1
fi

# Obtener el usuario real (no root)
REAL_USER=${SUDO_USER:-$USER}
REAL_HOME=$(eval echo ~$REAL_USER)
PROJECT_DIR="$REAL_HOME/MEGAsync/desarrollo/NetGui"

echo -e "${YELLOW}Instalando dependencias del sistema...${NC}"
apt update
apt install -y network-manager python3 python3-pip python3-venv network-manager-gnome

echo ""
echo -e "${YELLOW}Configurando entorno virtual Python...${NC}"
cd "$PROJECT_DIR"

# Crear entorno virtual como el usuario real, no como root
sudo -u $REAL_USER python3 -m venv venv

# Activar y instalar dependencias
sudo -u $REAL_USER bash -c "source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"

echo ""
echo -e "${YELLOW}Haciendo scripts ejecutables...${NC}"
chmod +x main.py
chmod +x network_manager.py

echo ""
echo -e "${YELLOW}Creando script de lanzamiento global...${NC}"
cat > /usr/local/bin/netgui << EOF
#!/bin/bash
cd "$PROJECT_DIR"
source venv/bin/activate
python3 main.py "\$@"
EOF

chmod +x /usr/local/bin/netgui

echo ""
echo -e "${YELLOW}Instalando integración con KDE...${NC}"
cp netgui.desktop /usr/share/applications/
update-desktop-database

echo ""
echo -e "${GREEN}======================================"
echo "   ✓ Instalación completada"
echo "======================================${NC}"
echo ""
echo "Puedes ejecutar NetGui de las siguientes formas:"
echo "  1. Desde terminal: netgui"
echo "  2. Desde el menú de aplicaciones de KDE"
echo "  3. Directamente: cd $PROJECT_DIR && source venv/bin/activate && python3 main.py"
echo ""
echo -e "${YELLOW}Documentación:${NC}"
echo "  Consulta la carpeta 'documentacion/' para guías completas"
echo "  README principal: $PROJECT_DIR/README.md"
echo ""
echo -e "${YELLOW}Nota:${NC} Para reiniciar interfaces sin contraseña (opcional):"
echo "  sudo visudo"
echo "  Agregar: $REAL_USER ALL=(ALL) NOPASSWD: /usr/bin/nmcli"
echo ""

