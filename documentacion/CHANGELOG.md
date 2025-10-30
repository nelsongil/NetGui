# Changelog

Todos los cambios notables en el proyecto NetGui se documentarán en este archivo.

## [1.3.0] - 2025-10-30

### 📦 Ejecutable Standalone

- ✨ **Generación de ejecutable con PyInstaller**:
  - Script automatizado `build_executable.sh` para compilar
  - Ejecutable de ~57MB con todas las dependencias incluidas
  - No requiere Python ni entorno virtual instalado
  - Compatible con sistemas Debian/KDE sin dependencias adicionales

- 🚀 **Script de instalación del ejecutable**:
  - `install_executable.sh` para instalar en `/usr/local/bin/`
  - Entrada automática en el menú de aplicaciones KDE
  - Archivo .desktop con icono y categorías correctas
  - Ejecución con `pkexec` para permisos de red

- 📝 **Documentación actualizada**:
  - README con instrucciones para generar ejecutable
  - Sección dedicada en la guía de inicio rápido
  - .gitignore actualizado para excluir archivos de compilación

### Ventajas del Ejecutable

- ✅ **Distribución simplificada**: Un solo archivo para compartir
- ✅ **Sin dependencias Python**: No requiere venv ni pip
- ✅ **Más rápido**: No necesita interpretar código
- ✅ **Instalación limpia**: Se integra perfectamente con el sistema

## [1.2.1] - 2025-10-30

### 📱 Mejoras de Responsive Design

- ✨ **Interfaz optimizada para diferentes tamaños de ventana**:
  - Tamaño mínimo ajustado: 950x650px (mejor que 800x600)
  - Tamaño inicial recomendado: 1100x700px
  - Ventana se abre con tamaño óptimo por defecto
  
- 🎯 **Botones optimizados para mejor adaptabilidad**:
  - Padding reducido: 10px-14px (antes 14px-18px)
  - Altura mínima: 36px (antes 42px)
  - Altura máxima: 48px (nueva restricción)
  - Fuente: 10pt (antes 11pt)
  - Bordes: 6px (antes 8px)
  - Espaciado entre botones: 6px (más compacto)
  
- 📊 **Panel de botones con límites de tamaño**:
  - Ancho mínimo: 220px
  - Ancho máximo: 280px
  - Evita que los botones se estiren o compriman demasiado
  
- 🔧 **Splitter optimizado**:
  - Proporción mejorada: 3:1 (lista:botones)
  - Tamaños iniciales sugeridos: 650px lista, 250px botones
  - Mejor distribución del espacio
  
- 📐 **Panel de información de red más compacto**:
  - Altura reducida: 150-175px (antes 160-210px)
  - Espaciado reducido: 4px entre elementos
  - Márgenes optimizados: 10px-8px
  - Fuentes ajustadas: 9pt contenido, 11pt perfil activo
  - Padding reducido en labels: 2px
  
- 🎨 **Elementos de título más compactos**:
  - Título principal: 16pt (antes 18pt), padding 12px (antes 15px)
  - Título lista perfiles: 11pt (antes 12pt), padding 8px (antes 10px)
  - Título panel info: 10pt (antes 11pt)
  
### Resultado

- ✅ **Mejor experiencia en ventanas pequeñas**: Los botones se ven bien sin pantalla completa
- ✅ **Mejor aprovechamiento del espacio**: Elementos más compactos pero legibles
- ✅ **Interfaz más balanceada**: Proporciones mejoradas entre secciones
- ✅ **Sin compromiso visual**: Mantiene el diseño outline y moderno

## [1.2.0] - 2025-10-30

### 🎨 Rediseño Completo - Botones Estilo Bootstrap Outline

- ✨ **Botones Outline implementados** (estilo Bootstrap):
  - **Fondo transparente** en estado normal
  - **Borde de 2px** en color específico de cada botón
  - **Texto del mismo color** que el borde
  - **Efecto hover**: Fondo se rellena con color, texto cambia a blanco
  - **Sombra con color** en hover (rgba del color principal)
  - **Efecto pressed**: Color más oscuro al presionar
  - Transiciones suaves y modernas
  
- 🎨 **Colores mantenidos pero con nuevo estilo**:
  - ✅ Activar: Verde (#4CAF50)
  - 📋 Duplicar: Azul claro (#03A9F4)
  - ✏️ Editar: Naranja (#FF9800)
  - ℹ️ Detalles: Morado (#9C27B0)
  - 🗑️ Eliminar: Rojo (#F44336)
  - 🔄 Actualizar: Gris (#607D8B)
  - ⚙️ Editor: Marrón (#795548)
  - ℹ️ Acerca de: Teal (#00897B)
  
- 💫 **Efectos visuales mejorados**:
  - Sombra con transparencia según el color del botón
  - Hover más pronunciado (sombra 4px)
  - Pressed con sombra reducida (2px)
  - Apariencia más ligera y moderna
  
- 📚 **Diálogos también actualizados**:
  - Botón "Documentación" en azul outline
  - Botón "Cerrar" en gris outline
  - Consistencia en toda la aplicación

### Características del Estilo Outline

**Estado Normal:**
```
┌─────────────────────────┐
│  ✅ Activar Perfil      │  ← Transparente, borde verde, texto verde
└─────────────────────────┘
```

**Estado Hover:**
```
┌─────────────────────────┐
│  ✅ Activar Perfil      │  ← Fondo verde, texto blanco, sombra verde
└─────────────────────────┘
```

**Estado Pressed:**
```
┌─────────────────────────┐
│  ✅ Activar Perfil      │  ← Fondo verde oscuro, sombra reducida
└─────────────────────────┘
```

### Ventajas del Nuevo Diseño

- 🎯 **Más moderno**: Sigue tendencias actuales de diseño
- 👁️ **Más limpio**: Fondo transparente reduce peso visual
- 🎨 **Más elegante**: Outline es más sofisticado que solid
- 🔍 **Mejor jerarquía**: Los botones no compiten por atención
- ✨ **Feedback claro**: El relleno al hover es muy intuitivo
- 🌈 **Colores destacan más**: El borde de color es más visible

### Mejorado

- 💅 Estética general más refinada y profesional
- 🎯 Mejor balance visual entre elementos
- 📱 Apariencia más moderna similar a frameworks web actuales

## [1.1.1] - 2025-10-30

### 🎨 Mejoras Visuales y UX

- ✨ **Botones mejorados significativamente**:
  - Mayor padding (14px-18px) para mejor clickabilidad
  - Bordes más redondeados (8px)
  - Sombras con efecto de elevación
  - Efectos dinámicos en hover (sombra más grande)
  - Efectos en pressed (sombra más pequeña, simula presión)
  - Altura mínima aumentada a 42px
  - Fuente 11pt (más legible)
  
- 📋 **Título añadido a la lista de perfiles**:
  - "Perfiles de Red Disponibles" con icono 📋
  - Fondo azul claro con borde redondeado
  - Mejor organización visual

- 🔍 **Filtrado inteligente de perfiles**:
  - Solo muestra WiFi y Ethernet
  - Excluye automáticamente: docker, bridges (br-*), loopback (lo), veth
  - Lista más limpia y relevante para el usuario
  - Evita confusión con dispositivos virtuales

- ℹ️ **Diálogo "Acerca de NetGui"** (nuevo):
  - Información completa de la aplicación
  - Versión actual destacada
  - Lista de características
  - Stack tecnológico
  - Información de licencia
  - Botón para abrir documentación
  - Diseño atractivo con gradientes

### 📁 Organización del Proyecto

- 📚 **Carpeta `documentacion/` creada**:
  - Todos los archivos .md movidos a carpeta dedicada
  - README.md en raíz simplificado (índice)
  - Mejor organización y estructura
  - Más fácil de mantener

- 📝 **Documentación reorganizada**:
  - README principal como punto de entrada
  - Referencias claras a documentación completa
  - Estructura más profesional

### Mejorado

- 🖱️ **Lista de perfiles más usable**:
  - Items con más padding (10px)
  - Margen entre items (3px)
  - Selección en negrita
  - Mejor feedback visual

- 📊 **Estructura de proyecto más clara**:
  - Separación entre código y documentación
  - Más fácil encontrar información
  - Profesional y organizado

### Agregado

- ➕ Botón "Acerca de NetGui" (color teal #00897B)
- ➕ Clase `AboutDialog` con toda la información de la app
- ➕ Separador visual antes del botón "Acerca de"
- ➕ Memoria guardada para futuros proyectos sobre organización de docs

## [1.1.0] - 2025-10-30

### 🎨 Mejoras Visuales Mayores

- ✨ **Interfaz completamente rediseñada**: Aspecto moderno y profesional
  - Esquema de colores Material Design
  - Bordes redondeados y sombras sutiles
  - Gradientes y efectos visuales atractivos
  
- 🔌 **Nombre del perfil activo prominente**: En el panel de información de red
  - Texto en negrita y tamaño grande
  - Destacado con color azul y fondo resaltado
  - Fácilmente distinguible del resto de la información
  
- 🎨 **Iconos visuales en toda la aplicación**:
  - **Panel de información**: 🔌 Perfil, 🌐 IP, 🚪 Gateway, 🔍 DNS, 🔌/📡 Interfaz
  - **Lista de perfiles**: 🟢 Activo, ⚪ Inactivo
  - **Tipos de conexión**: 📡 WiFi, 🔌 Ethernet, 🔒 VPN, 🌉 Bridge, 🔄 Loopback
  - **Botones**: ✅ Activar, 📋 Duplicar, ✏️ Editar, ℹ️ Detalles, 🗑️ Eliminar, 🔄 Actualizar, ⚙️ Editor
  - **Menú contextual**: Todos los elementos con iconos
  
- 🎨 **Botones con colores específicos**:
  - Verde (#4CAF50) para Activar
  - Azul claro (#03A9F4) para Duplicar
  - Naranja (#FF9800) para Editar
  - Morado (#9C27B0) para Ver Detalles
  - Rojo (#F44336) para Eliminar
  - Gris (#607D8B) para Actualizar
  - Marrón (#795548) para Editor Avanzado
  - Efectos hover y pressed en todos los botones
  
- 📊 **Panel de información de red mejorado**:
  - Borde verde con fondo gris claro
  - Título con icono 📡
  - Separador visual entre perfil y datos de red
  - Colores específicos para cada tipo de dato
  - Fondo azul claro para perfil activo
  
- 🎯 **Lista de perfiles mejorada**:
  - Perfiles activos en **negrita** y verde
  - Icono según tipo de conexión
  - Estado visual con 🟢 (activo) o ⚪ (inactivo)
  - Bordes redondeados en items seleccionados
  - Efecto hover al pasar el mouse
  - Fondo azul claro al seleccionar
  
- 🎨 **Título de la aplicación**:
  - Gradiente azul de fondo
  - Icono 🌐 NetGui destacado
  - Fuente más grande y atractiva
  
- 🖱️ **Menú contextual estilizado**:
  - Borde azul redondeado
  - Efectos hover en items
  - Separadores visuales
  - Iconos en todas las opciones

### Mejorado
- 💡 **Textos con mejor jerarquía visual**: Uso de negritas y colores para destacar información importante
- 🎯 **Interfaz más intuitiva**: Colores y iconos ayudan a identificar acciones rápidamente
- 📱 **Mejor experiencia de usuario**: Feedback visual claro en todas las interacciones

## [1.0.2] - 2025-10-30

### Agregado
- ✅ **Validación completa de datos**: Sistema de validación robusto antes de guardar cambios
  - Validación de formato de direcciones IP (xxx.xxx.xxx.xxx/xx)
  - Validación de formato de Gateway (xxx.xxx.xxx.xxx)
  - Validación de formato de DNS (soporta múltiples DNS separados por comas)
  - Validación de rangos (cada octeto entre 0-255, máscara entre /0 y /32)
  - Bloqueo de caracteres inválidos y letras en campos numéricos
- 🛡️ **Verificación de campos requeridos**: Para IP fija (manual)
  - Requiere dirección IP obligatoriamente
  - Advierte si falta Gateway o DNS (pero permite continuar)
  - Muestra ejemplos claros de formato correcto
- 📋 **Resumen de cambios**: Después de editar muestra un resumen de todos los cambios aplicados
- ℹ️ **Mensajes informativos mejorados**: Explicaciones claras de errores y recomendaciones

### Mejorado
- 🔧 **Guardado de datos para IP fija**: Corregido el guardado de configuración cuando se usa método "manual"
  - Ahora se guardan correctamente IP, Gateway y DNS para IP fija
  - Mejor manejo de datos según el método seleccionado
- 💬 **Feedback al usuario**: Mensajes más descriptivos sobre el resultado de las operaciones
  - Muestra exactamente qué cambios se aplicaron
  - Recuerda al usuario activar el perfil para aplicar cambios
  - Mensajes de error más informativos con sugerencias

### Corregido
- 🐛 **Edición no guardaba datos**: Corregido problema al cambiar a IP fija que no guardaba la configuración
- 🐛 **Datos no persistían**: Asegurado que todos los cambios se guarden correctamente en NetworkManager

## [1.0.1] - 2025-10-30

### Mejorado
- ✨ **Dropdown para método IPv4**: Ahora el método IPv4 se selecciona de un menú desplegable en lugar de escribir texto
  - Opciones: Automático (DHCP), Manual (IP Fija), Solo enlace local, Compartido, Deshabilitado
  - Más intuitivo y previene errores de escritura
- 🔧 **Corrección de información de red**: Mejorado el método para obtener IP, Gateway y DNS actual
  - Ahora muestra correctamente la información de red en el panel superior
  - Mejor manejo de múltiples interfaces
- 📝 **Mejores etiquetas**: El campo Gateway ahora dice claramente "Puerta de enlace (Gateway)"

### Corregido
- 🐛 Falta de importación de `Optional` que causaba error al iniciar
- 🐛 Panel de información de red mostrando "Sin conexión" cuando sí había conexión activa

## [1.0.0] - 2025-10-30

### Agregado
- ✨ Interfaz gráfica completa con PyQt6 para KDE Plasma
- 🌐 Panel de información de red en tiempo real (IP, Gateway, DNS, Interfaz)
- 🔍 Lista de perfiles de red con indicador de estado visual (activo/inactivo)
- 🔄 Activación de perfiles con un solo click o doble click
- 🔃 Reinicio automático de interfaces al cambiar perfiles
- 📋 Duplicación de perfiles de red existentes
- ✏️ Editor rápido para parámetros comunes (IP, DNS, Gateway)
- ⚙️ Integración con nm-connection-editor para edición avanzada
- 📊 Visor de detalles completos de configuración de perfiles
- 🗑️ Eliminación de perfiles con confirmación
- 🔄 Actualización automática de la lista cada 5 segundos
- 🔄 Actualización automática de información de red cada 3 segundos
- 🖱️ Menú contextual (click derecho) con todas las opciones
- 📱 Soporte para múltiples interfaces simultáneas
- 🎯 Priorización inteligente de interfaces (Ethernet sobre WiFi)
- 📝 Tooltips informativos para múltiples interfaces activas
- 🔐 Gestión completa de perfiles usando NetworkManager
- 📖 Documentación completa en español
- 🚀 Script de instalación automática
- ✅ Script de verificación de dependencias
- 📋 Archivo .desktop para integración con KDE
- 📄 Licencia MIT

### Características Técnicas
- Basado en NetworkManager (nmcli)
- Interfaz gráfica con PyQt6
- Compatible con Debian 13 (Trixie) y KDE Plasma 6
- Python 3.11+
- Actualización en tiempo real sin bloqueos
- Manejo robusto de errores
- Selección de texto en panel de información

### Documentación
- README.md completo con instrucciones detalladas
- QUICK_START.md para inicio rápido
- Script de instalación automática (install.sh)
- Script de verificación de dependencias (check_dependencies.py)
- Ejemplos de uso y casos comunes

## Próximas Características (Roadmap)

### [1.1.0] - Planificado
- [ ] Soporte para IPv6
- [ ] Gestión de conexiones VPN
- [ ] Perfiles favoritos con acceso rápido
- [ ] Importar/exportar perfiles
- [ ] Temas personalizables
- [ ] Notificaciones del sistema al cambiar perfil
- [ ] Estadísticas de uso de perfiles
- [ ] Programación automática de cambio de perfiles
- [ ] Detección automática de redes conocidas
- [ ] Modo "portátil" para laptop (cambio automático según ubicación)

### [1.2.0] - Planificado
- [ ] Indicador de systray para acceso rápido
- [ ] Atajos de teclado personalizables
- [ ] Backup y restauración de configuraciones
- [ ] Logs de cambios de perfiles
- [ ] Medidor de velocidad de red
- [ ] Prueba de conectividad (ping, traceroute)
- [ ] Escáner de redes WiFi disponibles
- [ ] Gestión de firewall básica

## Notas de Versión

### Versión 1.0.0
Primera versión estable de NetGui. Proporciona todas las funcionalidades básicas para gestionar perfiles de red en Debian 13 con KDE Plasma. La aplicación es totalmente funcional y lista para uso en producción.

**Características destacadas:**
- Monitor de red en tiempo real
- Cambio de perfil con un solo click
- Reinicio automático de interfaces
- Integración completa con NetworkManager

**Requisitos:**
- Debian 13 (Trixie) o superior
- KDE Plasma 6
- Python 3.11+
- NetworkManager

---

Para reportar bugs o sugerir características, por favor crea un issue en el repositorio del proyecto.

