# Guía de Interfaz de NetGui

## Vista General de la Interfaz

```
╔═══════════════════════════════════════════════════════════════╗
║              NetGui - Gestor de Perfiles de Red               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ Información de Red Actual                               │ ║
║  ├─────────────────────────────────────────────────────────┤ ║
║  │ IP: 192.168.1.100/24                                    │ ║
║  │ Gateway: 192.168.1.1                                    │ ║
║  │ DNS: 8.8.8.8, 8.8.4.4                                   │ ║
║  │ Interfaz: enp0s3 (ethernet) - connected                 │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
║  ┌─────────────────────────────┬─────────────────────────┐   ║
║  │ Lista de Perfiles           │  Acciones               │   ║
║  ├─────────────────────────────┼─────────────────────────┤   ║
║  │                             │                         │   ║
║  │ ● Red Casa (ethernet)       │  ✓ Activar Perfil      │   ║
║  │   - enp0s3                  │                         │   ║
║  │                             │  ⎘ Duplicar Perfil     │   ║
║  │ ○ Red Trabajo (ethernet)    │                         │   ║
║  │   - enp0s3                  │  ✎ Editar Perfil       │   ║
║  │                             │                         │   ║
║  │ ○ WiFi Casa (wifi)          │  ⓘ Ver Detalles        │   ║
║  │   - wlan0                   │                         │   ║
║  │                             │  🗑 Eliminar Perfil     │   ║
║  │ ○ Red Casa - IP Fija        │                         │   ║
║  │   - enp0s3                  │                         │   ║
║  │                             │                         │   ║
║  │                             │  ↻ Actualizar Lista     │   ║
║  │                             │                         │   ║
║  │                             │  ⚙ Abrir               │   ║
║  │                             │    nm-connection-editor │   ║
║  │                             │                         │   ║
║  └─────────────────────────────┴─────────────────────────┘   ║
║                                                               ║
║  Estado: Perfiles cargados: 4                                 ║
╚═══════════════════════════════════════════════════════════════╝
```

## Componentes de la Interfaz

### 1. Panel de Información de Red (Superior)

**Ubicación:** Parte superior de la ventana

**Contenido:**
- **IP actual**: Dirección IP asignada a tu interfaz principal
  - Formato: `192.168.1.100/24` (IP/máscara de red)
  - Si tienes múltiples interfaces, pasa el cursor sobre este campo para ver todas
  
- **Gateway**: Puerta de enlace predeterminada
  - Tu router o punto de salida a Internet
  
- **DNS**: Servidores DNS configurados
  - Separados por comas si hay múltiples
  
- **Interfaz**: Dispositivo de red activo
  - Nombre del dispositivo (ej: enp0s3, wlan0)
  - Tipo (ethernet, wifi, etc.)
  - Estado de conexión

**Actualización:** Se actualiza automáticamente cada 3 segundos

**Características:**
- ✅ El texto es seleccionable (puedes copiarlo)
- ✅ Muestra la interfaz más relevante (prioriza Ethernet sobre WiFi)
- ✅ Tooltip con información de todas las interfaces si hay múltiples

### 2. Lista de Perfiles (Izquierda)

**Ubicación:** Lado izquierdo de la ventana principal

**Formato de cada entrada:**
```
[Estado] Nombre del Perfil (Tipo)
         - Dispositivo asociado
```

**Indicadores de estado:**
- `●` (punto lleno verde) = Perfil activo
- `○` (punto vacío) = Perfil inactivo

**Tipos comunes:**
- `ethernet` - Conexión por cable
- `wifi` - Conexión inalámbrica
- `vpn` - Red privada virtual
- `bridge` - Puente de red

**Interacciones:**
- **Click simple**: Selecciona el perfil
- **Doble click**: Activa el perfil seleccionado
- **Click derecho**: Abre menú contextual con todas las opciones

### 3. Panel de Botones (Derecha)

**Ubicación:** Lado derecho de la ventana principal

#### Botones de Acción sobre Perfiles:

**✓ Activar Perfil**
- Activa el perfil seleccionado
- Desactiva automáticamente el perfil anterior (si aplica)
- Reinicia la interfaz de red
- Atajo: Doble click en el perfil

**⎘ Duplicar Perfil**
- Crea una copia del perfil seleccionado
- Te pide un nombre para el nuevo perfil
- Útil para crear variantes (ej: DHCP vs IP fija)

**✎ Editar Perfil**
- Abre diálogo de edición rápida
- Permite cambiar: nombre, IP, gateway, DNS, método IPv4
- Botón para abrir editor avanzado (nm-connection-editor)

**ⓘ Ver Detalles**
- Muestra toda la configuración del perfil
- Incluye UUID, tipo, y todos los parámetros
- Modo solo lectura

**🗑 Eliminar Perfil**
- Elimina el perfil seleccionado
- Solicita confirmación
- ⚠️ Acción irreversible

#### Botones de Gestión General:

**↻ Actualizar Lista**
- Recarga manualmente la lista de perfiles
- También actualiza información de red
- Útil si haces cambios externos

**⚙ Abrir nm-connection-editor**
- Abre la herramienta oficial de NetworkManager
- Para configuración avanzada completa
- Se ejecuta como proceso separado

### 4. Barra de Estado (Inferior)

**Ubicación:** Parte inferior de la ventana

**Muestra:**
- Mensajes de operaciones (ej: "Activando perfil...")
- Resultados de acciones (ej: "Perfil activado")
- Número de perfiles cargados
- Errores temporales

**Duración:** Los mensajes se muestran por 3-5 segundos

## Menú Contextual (Click Derecho)

Al hacer click derecho en cualquier perfil:

```
┌─────────────────────────┐
│ Activar                 │
├─────────────────────────┤
│ Duplicar                │
│ Editar                  │
│ Ver Detalles            │
├─────────────────────────┤
│ Eliminar                │
└─────────────────────────┘
```

Mismas funciones que los botones, pero más rápido de acceder.

## Diálogos

### Diálogo de Duplicación

```
┌────────────────────────────────────────┐
│ Duplicar Perfil                        │
├────────────────────────────────────────┤
│                                        │
│ Nombre del nuevo perfil:              │
│ ┌────────────────────────────────────┐ │
│ │ Red Casa (copia)                   │ │
│ └────────────────────────────────────┘ │
│                                        │
│              [Aceptar] [Cancelar]      │
└────────────────────────────────────────┘
```

### Diálogo de Edición Rápida

```
┌─────────────────────────────────────────────────┐
│ Editar: Red Casa                                │
├─────────────────────────────────────────────────┤
│ Edición rápida de parámetros comunes           │
│ Para edición avanzada, usa el botón inferior   │
│                                                 │
│ Configuración IPv4                             │
│ ┌───────────────────────────────────────────┐  │
│ │ Método IPv4:    [auto/manual/disabled]    │  │
│ │ Dirección IP:   [192.168.1.100/24]        │  │
│ │ Puerta enlace:  [192.168.1.1]             │  │
│ │ Servidores DNS: [8.8.8.8,8.8.4.4]         │  │
│ └───────────────────────────────────────────┘  │
│                                                 │
│ [Editor Avanzado] [Aceptar] [Cancelar]         │
└─────────────────────────────────────────────────┘
```

### Diálogo de Detalles

```
┌─────────────────────────────────────────────────┐
│ Detalles: Red Casa                              │
├─────────────────────────────────────────────────┤
│                                                 │
│ Perfil: Red Casa                                │
│ UUID: a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6     │
│ Tipo: ethernet                                  │
│ Dispositivo: enp0s3                             │
│ Estado: Activo                                  │
│ ─────────────────────────────────────────────   │
│                                                 │
│ Configuración completa:                         │
│ connection.id: Red Casa                         │
│ connection.uuid: a1b2c3d4-e5f6-g7h8...         │
│ connection.type: 802-3-ethernet                 │
│ ipv4.method: auto                               │
│ ipv4.dns: 8.8.8.8,8.8.4.4                      │
│ [... más detalles ...]                          │
│                                                 │
│                              [Cerrar]           │
└─────────────────────────────────────────────────┘
```

## Indicadores Visuales

### Colores

- **Verde oscuro**: Perfil activo en la lista
- **Negro**: Perfil inactivo
- **Verde (●)**: Indicador de perfil activo
- **Gris (○)**: Indicador de perfil inactivo

### Símbolos

- `●` Perfil activo
- `○` Perfil inactivo
- `✓` Activar
- `⎘` Duplicar
- `✎` Editar
- `ⓘ` Información
- `🗑` Eliminar
- `↻` Actualizar
- `⚙` Configuración

## Atajos y Tips

### Atajos Rápidos

- **Doble click**: Activa perfil
- **Click derecho**: Menú contextual
- **Selección de texto**: Puedes copiar IPs y datos del panel superior

### Tips de Uso

1. **Múltiples interfaces**: Si tienes Ethernet y WiFi activos, pasa el cursor sobre la IP para ver ambas
2. **Actualización automática**: No necesitas refrescar manualmente, todo se actualiza solo
3. **Editor avanzado**: Para VPN, bridges, o configuración compleja, usa nm-connection-editor
4. **Tooltips**: Pasa el cursor sobre elementos para ver información adicional
5. **Nombres descriptivos**: Usa nombres claros al duplicar (ej: "Casa-DHCP", "Casa-IPFija")

## Flujo de Trabajo Típico

### Crear perfil alternativo:
1. Selecciona perfil actual
2. Click en "Duplicar"
3. Asigna nombre descriptivo
4. Click en "Editar"
5. Modifica parámetros
6. Guarda cambios

### Cambiar entre perfiles:
1. Doble click en el perfil deseado
2. Espera 2-3 segundos
3. Verifica el cambio en el panel superior
4. ¡Listo!

### Verificar configuración:
1. Mira el panel superior para IP/Gateway/DNS
2. Click en "Ver Detalles" para configuración completa
3. Usa nm-connection-editor para edición avanzada

---

**Nota**: Esta interfaz está optimizada para KDE Plasma y sigue las guías de diseño de Qt6.

