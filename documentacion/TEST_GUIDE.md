# Guía de Pruebas - NetGui

Esta guía te ayudará a verificar que NetGui funciona correctamente en tu sistema.

## Pre-requisitos de Prueba

Antes de comenzar las pruebas, asegúrate de:

```bash
# 1. Verificar que NetworkManager está activo
systemctl status NetworkManager

# 2. Verificar que tienes perfiles de red existentes
nmcli connection show

# 3. Verificar que nm-connection-editor está instalado
which nm-connection-editor
```

## Paso 1: Verificación de Dependencias

```bash
cd /home/nelson/MEGAsync/desarrollo/NetGui
python3 check_dependencies.py
```

**Resultado esperado:** Todas las dependencias deben mostrar ✓

**Si falla:**
```bash
# Instalar dependencias faltantes
sudo apt install network-manager python3 python3-pip python3-venv network-manager-gnome

# Crear entorno virtual y instalar paquetes Python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Paso 2: Primera Ejecución

```bash
source venv/bin/activate
python3 main.py
```

**Qué verificar:**

### ✅ Ventana Principal
- [ ] La aplicación se abre sin errores
- [ ] El título muestra "NetGui - Gestor de Perfiles de Red"
- [ ] La ventana tiene tamaño adecuado (800x600 mínimo)

### ✅ Panel de Información de Red
- [ ] Se muestra en la parte superior
- [ ] Muestra tu IP actual (no "Cargando...")
- [ ] Muestra Gateway (si está configurado)
- [ ] Muestra DNS (si está configurado)
- [ ] Muestra interfaz activa (ej: enp0s3, wlan0)

### ✅ Lista de Perfiles
- [ ] Muestra al menos un perfil de red
- [ ] Los perfiles activos tienen el símbolo ● en verde
- [ ] Los perfiles inactivos tienen el símbolo ○
- [ ] Se muestra el tipo de conexión (ethernet, wifi, etc.)

### ✅ Botones
- [ ] Todos los botones son visibles
- [ ] Los botones tienen los iconos correctos

## Paso 3: Pruebas Funcionales

### Test 1: Actualización Automática

**Objetivo:** Verificar que la información se actualiza automáticamente

**Pasos:**
1. Deja la aplicación abierta
2. Espera 5 segundos
3. Observa la barra de estado

**Resultado esperado:**
- La barra de estado debe mostrar "Perfiles cargados: X" periódicamente
- El panel de IP debe actualizarse cada 3 segundos

### Test 2: Ver Detalles de Perfil

**Pasos:**
1. Selecciona cualquier perfil de la lista
2. Click en "Ver Detalles"

**Resultado esperado:**
- Se abre un diálogo con información detallada
- Muestra UUID, tipo, estado, configuración completa
- El botón "Cerrar" funciona

**Si falla:** Verifica que tienes permisos para leer configuración de NetworkManager

### Test 3: Duplicar Perfil

**Pasos:**
1. Selecciona un perfil existente (preferiblemente uno no activo)
2. Click en "Duplicar Perfil"
3. Ingresa nombre: "Test Duplicado"
4. Click "Aceptar"

**Resultado esperado:**
- Mensaje de éxito
- El nuevo perfil "Test Duplicado" aparece en la lista
- Puedes seleccionarlo

**Si falla:** Verifica permisos de NetworkManager

**Limpieza:**
```bash
# Eliminar el perfil de prueba
nmcli connection delete "Test Duplicado"
```

### Test 4: Edición Rápida

**⚠️ Nota:** Este test modifica un perfil. Usa el perfil duplicado del Test 3.

**Pasos:**
1. Selecciona "Test Duplicado"
2. Click en "Editar Perfil"
3. Cambia el nombre a "Test Editado"
4. Cambia método IPv4 a "manual"
5. Ingresa IP: 192.168.100.100/24
6. Click "Aceptar"

**Resultado esperado:**
- Mensaje de éxito
- El perfil cambia de nombre en la lista
- Los cambios se guardan

**Verificar:**
```bash
nmcli connection show "Test Editado"
```

**Limpieza:**
```bash
nmcli connection delete "Test Editado"
```

### Test 5: Activar Perfil

**⚠️ IMPORTANTE:** Este test cambiará tu conexión de red activa. Asegúrate de:
- Tener un perfil de respaldo
- Saber cómo volver a tu configuración original
- No estar en SSH o conexión remota crítica

**Pasos:**
1. Anota tu perfil actual activo
2. Selecciona otro perfil de la lista
3. Doble click en el perfil (o botón "Activar")
4. Espera 3-5 segundos

**Resultado esperado:**
- Mensaje de confirmación
- El nuevo perfil muestra ● (activo)
- El perfil anterior muestra ○ (inactivo)
- El panel de IP se actualiza con la nueva configuración
- La interfaz se reinicia automáticamente

**Restaurar conexión original:**
1. Doble click en tu perfil original
2. O desde terminal: `nmcli connection up "nombre-perfil-original"`

### Test 6: Menú Contextual

**Pasos:**
1. Click derecho en cualquier perfil
2. Observa el menú

**Resultado esperado:**
- Aparece menú con opciones: Activar, Duplicar, Editar, Ver Detalles, Eliminar
- Las opciones funcionan igual que los botones

### Test 7: Editor Avanzado

**Pasos:**
1. Click en "Abrir nm-connection-editor"

**Resultado esperado:**
- Se abre la aplicación nm-connection-editor
- Puedes ver y editar perfiles
- Se ejecuta como proceso independiente

**Si falla:** 
```bash
sudo apt install network-manager-gnome
```

### Test 8: Eliminar Perfil

**⚠️ ADVERTENCIA:** Solo elimina perfiles de prueba, no perfiles importantes

**Pasos:**
1. Crea un perfil de prueba:
```bash
nmcli connection add type ethernet con-name "Perfil-Test-Borrar" ifname enp0s3
```
2. Click "Actualizar Lista" en NetGui
3. Selecciona "Perfil-Test-Borrar"
4. Click "Eliminar Perfil"
5. Confirma la eliminación

**Resultado esperado:**
- Diálogo de confirmación
- Mensaje de éxito
- El perfil desaparece de la lista

### Test 9: Múltiples Interfaces

**Requisito:** Tener Ethernet y WiFi activos simultáneamente

**Pasos:**
1. Activa tanto Ethernet como WiFi
2. Observa el panel de información de red
3. Pasa el cursor sobre la IP

**Resultado esperado:**
- Muestra la IP de la interfaz prioritaria (Ethernet)
- El tooltip muestra información de ambas interfaces

### Test 10: Información en Tiempo Real

**Pasos:**
1. Mantén NetGui abierto
2. Desde terminal, cambia de perfil:
```bash
nmcli connection up "otro-perfil"
```
3. Observa NetGui

**Resultado esperado:**
- En 5 segundos o menos, la lista se actualiza
- El panel de IP se actualiza en 3 segundos
- Los indicadores ● y ○ se actualizan correctamente

## Paso 4: Pruebas de Estrés

### Test de Múltiples Cambios Rápidos

**Pasos:**
1. Cambia entre 3-4 perfiles rápidamente (cada 2 segundos)
2. Observa la aplicación

**Resultado esperado:**
- La aplicación no se congela
- Los cambios se procesan en orden
- No hay errores en terminal

### Test de Ejecución Prolongada

**Pasos:**
1. Deja NetGui abierto por 10-15 minutos
2. Observa uso de CPU y memoria

**Resultado esperado:**
- Uso de CPU bajo (< 5% en inactividad)
- Uso de memoria estable (< 100 MB)
- Sin memory leaks
- Las actualizaciones siguen funcionando

## Paso 5: Verificación de Instalación Global

```bash
# Instalar globalmente
sudo ./install.sh

# Probar comando global
netgui

# Verificar integración KDE
# Busca "NetGui" en el menú de aplicaciones de KDE
```

**Resultado esperado:**
- Instalación sin errores
- El comando `netgui` funciona desde cualquier directorio
- Aparece en el menú de aplicaciones de KDE

## Checklist Final

Antes de considerar NetGui completamente funcional:

### Funcionalidad Básica
- [ ] La aplicación inicia sin errores
- [ ] Muestra IP actual correctamente
- [ ] Lista todos los perfiles de NetworkManager
- [ ] Identifica perfiles activos/inactivos
- [ ] Panel de información se actualiza automáticamente
- [ ] Lista de perfiles se actualiza automáticamente

### Operaciones sobre Perfiles
- [ ] Duplicar perfil funciona
- [ ] Editar perfil funciona
- [ ] Ver detalles funciona
- [ ] Activar perfil funciona y reinicia interfaz
- [ ] Eliminar perfil funciona
- [ ] Menú contextual funciona

### Integraciones
- [ ] nm-connection-editor se abre correctamente
- [ ] Funciona con NetworkManager del sistema
- [ ] Se integra con KDE Plasma

### Estabilidad
- [ ] No hay crashes durante uso normal
- [ ] Maneja errores gracefully
- [ ] No causa problemas de red

## Solución de Problemas Comunes

### Error: "Could not connect to NetworkManager"

**Solución:**
```bash
sudo systemctl start NetworkManager
sudo systemctl enable NetworkManager
```

### Error: "PyQt6 not found"

**Solución:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Error: "Permission denied" al activar perfiles

**Solución:**
```bash
# Agregar usuario al grupo necesario
sudo usermod -aG netdev $USER

# O configurar polkit (más seguro)
# Crear: /etc/polkit-1/rules.d/50-network-manager.rules
```

### La IP no se muestra

**Verificar:**
```bash
# Verifica que tienes conexión
ip addr show

# Verifica NetworkManager
nmcli device status

# Ejecuta NetGui desde terminal para ver errores
python3 main.py
```

### Perfiles no aparecen en la lista

**Verificar:**
```bash
# Ver perfiles desde terminal
nmcli connection show

# Si hay perfiles pero no aparecen en NetGui
# verifica permisos y reinicia NetworkManager
sudo systemctl restart NetworkManager
```

## Reporte de Bugs

Si encuentras problemas:

1. **Captura la salida de terminal:**
```bash
python3 main.py 2>&1 | tee netgui-debug.log
```

2. **Información del sistema:**
```bash
uname -a
lsb_release -a
nmcli --version
python3 --version
pip list | grep PyQt6
```

3. **Estado de NetworkManager:**
```bash
systemctl status NetworkManager
nmcli connection show
nmcli device status
```

4. Incluye toda esta información al reportar el bug

---

**¡Buena suerte con las pruebas!** 🚀

Si todos los tests pasan, NetGui está listo para uso en producción.

