# Guía de Validación de Datos - NetGui

Esta guía explica las validaciones que NetGui aplica cuando editas perfiles de red.

## 🛡️ Sistema de Validación

NetGui valida automáticamente todos los datos antes de guardar cambios para prevenir errores de configuración.

## 📝 Formatos Válidos

### 1. Dirección IP

**Formato válido:**
```
192.168.1.100/24
```

**Componentes:**
- **IP**: Cuatro números separados por puntos (xxx.xxx.xxx.xxx)
- **Máscara**: Slash seguido de número (/xx) - OPCIONAL

**Reglas:**
- ✅ Cada número debe estar entre 0 y 255
- ✅ La máscara debe estar entre /0 y /32
- ✅ Puede omitir la máscara: `192.168.1.100`
- ❌ No puede contener letras
- ❌ No puede tener más de 4 octetos

**Ejemplos válidos:**
```
192.168.1.100/24   ✓ IP con máscara /24
192.168.0.50/16    ✓ IP con máscara /16
10.0.0.1/8         ✓ IP con máscara /8
192.168.1.100      ✓ IP sin máscara (válido pero no recomendado)
172.16.0.1/32      ✓ IP con máscara /32
```

**Ejemplos inválidos:**
```
192.168.1.256/24   ✗ 256 excede el límite (máx 255)
192.168.1.100/33   ✗ Máscara /33 excede /32
192.168.1          ✗ Falta el cuarto octeto
192.168.1.abc/24   ✗ Contiene letras
192.168.1.100.1/24 ✗ Tiene 5 octetos
```

### 2. Gateway (Puerta de enlace)

**Formato válido:**
```
192.168.1.1
```

**Componentes:**
- Cuatro números separados por puntos (xxx.xxx.xxx.xxx)
- NO lleva máscara de red

**Reglas:**
- ✅ Cada número debe estar entre 0 y 255
- ✅ Exactamente 4 octetos
- ❌ No puede contener letras
- ❌ No lleva máscara (/xx)

**Ejemplos válidos:**
```
192.168.1.1        ✓ Gateway típico de red doméstica
192.168.0.1        ✓ Gateway alternativo común
10.0.0.1           ✓ Gateway de red corporativa
172.16.0.1         ✓ Gateway válido
```

**Ejemplos inválidos:**
```
192.168.1.1/24     ✗ No debe llevar máscara
192.168.1.256      ✗ 256 excede el límite
192.168.1          ✗ Falta el cuarto octeto
192.168.1.1.1      ✗ Tiene 5 octetos
gateway.local      ✗ No se permiten nombres, solo IPs
```

### 3. Servidores DNS

**Formato válido:**
```
8.8.8.8,8.8.4.4
```

**Componentes:**
- Una o más direcciones IP
- Separadas por comas si hay múltiples
- Cada IP con cuatro números separados por puntos

**Reglas:**
- ✅ Cada número debe estar entre 0 y 255
- ✅ Múltiples DNS separados por comas
- ✅ Espacios después de las comas son opcionales
- ❌ No puede contener letras
- ❌ No lleva máscara (/xx)

**Ejemplos válidos:**
```
8.8.8.8                      ✓ Un solo DNS (Google)
8.8.8.8,8.8.4.4             ✓ Dos DNS de Google
1.1.1.1,1.0.0.1             ✓ DNS de Cloudflare
8.8.8.8, 8.8.4.4            ✓ Con espacio después de coma
208.67.222.222,208.67.220.220 ✓ DNS de OpenDNS
```

**Ejemplos inválidos:**
```
8.8.8.8,8.8.4.256           ✗ 256 excede el límite
8.8.8.8;8.8.4.4             ✗ Debe usar comas, no punto y coma
google-dns                  ✗ No se permiten nombres
8.8.8.8/24                  ✗ No debe llevar máscara
8.8.8,8.8.4.4               ✗ Falta octeto en primera IP
```

## 🎯 Validaciones Especiales para IP Fija (Manual)

Cuando seleccionas **"Manual - IP Fija"** en el método IPv4:

### ✅ Campo Requerido

**Dirección IP**: OBLIGATORIO
```
Si no ingresas una IP, NetGui te mostrará:

"Para usar IP fija (manual) debes especificar:
• Dirección IP (requerido)
• Gateway (recomendado)
• DNS (recomendado)"
```

### ⚠️ Campos Recomendados

**Gateway y DNS**: RECOMENDADOS pero NO obligatorios

Si faltan, NetGui preguntará:
```
"Has seleccionado IP fija (manual) pero falta:
• Gateway
• Servidores DNS

¿Deseas continuar de todas formas?

La conexión podría no funcionar correctamente sin estos datos."
```

Puedes elegir:
- **Sí**: Continúa sin Gateway/DNS (no recomendado)
- **No**: Vuelve al formulario para completar los datos

## 🚫 Errores Comunes y Soluciones

### Error: "La dirección IP no es válida"

**Causas:**
- Números mayores a 255
- Formato incorrecto
- Letras o caracteres especiales
- Máscara incorrecta

**Solución:**
```
✗ 192.168.1.300/24  → ✓ 192.168.1.100/24
✗ 192.168.1.abc/24  → ✓ 192.168.1.100/24
✗ 192.168.1/24      → ✓ 192.168.1.100/24
✗ 192.168.1.100/40  → ✓ 192.168.1.100/24
```

### Error: "El gateway no es válido"

**Causas:**
- Incluye máscara de red (no debe llevarla)
- Números mayores a 255
- Formato incorrecto

**Solución:**
```
✗ 192.168.1.1/24   → ✓ 192.168.1.1
✗ 192.168.1.256    → ✓ 192.168.1.1
✗ 192.168.1        → ✓ 192.168.1.1
```

### Error: "Los servidores DNS no son válidos"

**Causas:**
- Formato incorrecto en algún DNS
- Separador incorrecto (debe ser coma)
- Números mayores a 255

**Solución:**
```
✗ 8.8.8.8;8.8.4.4       → ✓ 8.8.8.8,8.8.4.4
✗ 8.8.8.256,8.8.4.4     → ✓ 8.8.8.8,8.8.4.4
✗ 8.8.8,8.8.4.4         → ✓ 8.8.8.8,8.8.4.4
```

## 📚 Ejemplos Completos de Configuración

### Ejemplo 1: Red Doméstica con IP Fija

```
Método IPv4: Manual - IP Fija
Dirección IP: 192.168.1.100/24
Gateway: 192.168.1.1
DNS: 8.8.8.8,8.8.4.4
```

### Ejemplo 2: Red Corporativa

```
Método IPv4: Manual - IP Fija
Dirección IP: 10.20.30.50/16
Gateway: 10.20.0.1
DNS: 10.20.0.10,10.20.0.11
```

### Ejemplo 3: Servidor con DNS Cloudflare

```
Método IPv4: Manual - IP Fija
Dirección IP: 172.16.0.100/24
Gateway: 172.16.0.1
DNS: 1.1.1.1,1.0.0.1
```

### Ejemplo 4: DHCP (Automático)

```
Método IPv4: Automático - DHCP (recomendado)
Dirección IP: (dejar vacío)
Gateway: (dejar vacío)
DNS: (dejar vacío o especificar si quieres DNS personalizados)
```

## 🔍 Entendiendo las Máscaras de Red

| Máscara | Hosts disponibles | Uso típico |
|---------|-------------------|------------|
| /24     | 254 hosts         | Red doméstica pequeña |
| /16     | 65,534 hosts      | Red mediana/corporativa |
| /8      | 16,777,214 hosts  | Red grande |
| /32     | 1 host (solo esta IP) | Host único |

**Máscaras comunes:**
- `/24` = 255.255.255.0 (más común en redes domésticas)
- `/16` = 255.255.0.0
- `/8` = 255.0.0.0

## ⚡ Tips Rápidos

### ✅ Buenas Prácticas

1. **Siempre usa máscara de red**: Especifica /24 en redes domésticas
2. **Verifica el gateway**: Debe estar en la misma red que tu IP
3. **Usa DNS confiables**: Google (8.8.8.8) o Cloudflare (1.1.1.1)
4. **Evita IPs en uso**: Verifica que tu IP fija no esté siendo usada por otro dispositivo

### ❌ Errores a Evitar

1. **No uses IPs fuera de rango**: Respeta tu rango de red local
2. **No omitas la máscara**: Siempre especifica /24, /16, etc.
3. **No uses gateway incorrecto**: Debe ser la IP de tu router
4. **No uses DNS inaccesibles**: Verifica que los DNS funcionen

## 🆘 ¿Qué hacer si hay errores?

1. **Lee el mensaje de error**: NetGui te indica exactamente qué está mal
2. **Verifica el formato**: Usa los ejemplos de esta guía
3. **Copia y pega**: Reduce errores de escritura
4. **Usa el editor avanzado**: Para configuraciones complejas, usa nm-connection-editor

## 📞 Verificar Configuración

Después de guardar, puedes verificar con:

```bash
# Ver configuración del perfil
nmcli connection show "nombre-del-perfil" | grep ipv4

# Ver IP actual
ip addr show

# Probar conectividad
ping -c 4 8.8.8.8
```

---

**Recuerda**: NetGui valida automáticamente todos estos campos. Si algo está mal, te lo indicará antes de guardar. 🛡️

