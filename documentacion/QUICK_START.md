# NetGui - Guía de Inicio Rápido

## Instalación Rápida

```bash
# 1. Instalar con el script automático (recomendado)
cd /home/nelson/MEGAsync/desarrollo/NetGui
sudo ./install.sh

# 2. Ejecutar la aplicación
netgui
```

## Instalación Manual

Si prefieres instalar manualmente:

```bash
# 1. Instalar dependencias del sistema
sudo apt update
sudo apt install network-manager python3 python3-pip python3-venv network-manager-gnome

# 2. Crear entorno virtual
cd /home/nelson/MEGAsync/desarrollo/NetGui
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias Python
pip install -r requirements.txt

# 4. Ejecutar
python3 main.py
```

## Uso Básico

### Interfaz Principal

Al abrir NetGui verás:

- **Panel de Información de Red** (arriba): Muestra tu IP actual, gateway, DNS e interfaz en tiempo real
- **Lista de Perfiles** (centro): Todos tus perfiles con indicador de estado (● activo / ○ inactivo)
- **Botones de Acción** (derecha): Todas las operaciones disponibles

La información se actualiza automáticamente:
- IP y datos de red: cada 3 segundos
- Lista de perfiles: cada 5 segundos

### 1. Cambiar de perfil de red

```
1. Abre NetGui
2. Selecciona el perfil deseado de la lista
3. Haz doble click o presiona "Activar Perfil"
4. ¡Listo! La interfaz se reinicia automáticamente
```

### 2. Crear un perfil alternativo

```
1. Selecciona tu perfil actual (ej: "Red Casa")
2. Click en "Duplicar Perfil"
3. Nómbralo (ej: "Red Casa - IP Fija")
4. Click en "Editar Perfil"
5. Cambia la configuración (IP estática, DNS personalizado, etc.)
6. Guarda los cambios
```

### 3. Ejemplo de uso común: Red Casa vs Red Trabajo

**Escenario**: Necesitas diferentes configuraciones de red en casa y en el trabajo.

```
Paso 1: Duplicar perfil actual
  - Selecciona "Red Casa"
  - Duplicar → "Red Trabajo"

Paso 2: Editar "Red Trabajo"
  - Seleccionar "Red Trabajo"
  - Editar Perfil
  - Cambiar:
    * Método IPv4: manual
    * Dirección IP: 192.168.1.100/24
    * Gateway: 192.168.1.1
    * DNS: 8.8.8.8,8.8.4.4
  - Guardar

Paso 3: Cambiar entre perfiles
  - En casa: Doble click en "Red Casa"
  - En trabajo: Doble click en "Red Trabajo"
```

## Casos de Uso

### 🏠 Diferentes redes WiFi

Crea perfiles separados para cada red WiFi que uses frecuentemente:
- Casa
- Trabajo
- Cafetería favorita
- etc.

### 🌐 IP estática vs DHCP

Duplica un perfil y configura uno con IP estática y otro con DHCP:
- "Red Principal - DHCP"
- "Red Principal - IP Fija"

### 🔒 Diferentes servidores DNS

Crea perfiles con diferentes DNS:
- "Internet Normal" (DNS del ISP)
- "Internet Rápido" (Google DNS: 8.8.8.8)
- "Internet Privado" (Cloudflare: 1.1.1.1)

### 🎮 Gaming vs Streaming

Optimiza diferentes perfiles:
- "Gaming" (baja latencia, QoS configurado)
- "Streaming" (ancho de banda prioritario)

## Atajos de Teclado

Cuando la aplicación esté en foco:

- **Doble click**: Activar perfil seleccionado
- **Click derecho**: Menú contextual con todas las opciones
- **Actualización**: Lista se actualiza automáticamente cada 5 segundos

## Consejos

### ✅ Mejores Prácticas

1. **Nombres descriptivos**: Usa nombres claros como "Casa-DHCP" o "Trabajo-IPFija"
2. **Mantén backups**: Antes de eliminar, duplica perfiles importantes
3. **Prueba los cambios**: Después de editar, verifica la conexión
4. **Usa el editor avanzado**: Para configuración compleja (VPN, bridges, etc.)

### ⚠️ Advertencias

1. **No elimines perfiles activos** sin tener un respaldo
2. **Ten cuidado con IP fijas** en redes DHCP (pueden causar conflictos)
3. **Verifica los permisos** si tienes problemas para activar perfiles

## Solución Rápida de Problemas

### No puedo activar un perfil

```bash
# Verifica que NetworkManager esté corriendo
systemctl status NetworkManager

# Si no está activo
sudo systemctl start NetworkManager
```

### La interfaz no se actualiza

```bash
# Reinicia manualmente
sudo nmcli device connect <nombre-interfaz>

# O reinicia NetworkManager
sudo systemctl restart NetworkManager
```

### El editor avanzado no abre

```bash
# Instala nm-connection-editor
sudo apt install network-manager-gnome
```

## Desinstalación

Si necesitas desinstalar NetGui:

```bash
# Eliminar script global
sudo rm /usr/local/bin/netgui

# Eliminar integración KDE
sudo rm /usr/share/applications/netgui.desktop
sudo update-desktop-database

# Eliminar proyecto (opcional)
rm -rf /home/nelson/MEGAsync/desarrollo/NetGui
```

## Soporte

Para reportar problemas o sugerencias:
1. Revisa la documentación completa en `README.md`
2. Verifica los logs del sistema: `journalctl -u NetworkManager`
3. Ejecuta en terminal para ver errores: `python3 main.py`

---

¡Disfruta de NetGui! 🚀

