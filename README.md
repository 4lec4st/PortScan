# Port Scanner

## Descripción
Este script realiza un escaneo de puertos en un host objetivo utilizando sockets en Python y concurrencia con ThreadPoolExecutor. Es útil para evaluar la exposición de servicios en una red.

## Requisitos
- Python 3.x
- Permisos de superusuario (root) si se escanean puertos restringidos (<1024)

## Instalación
1. Clona el repositorio o guarda el script en tu máquina.
2. Asegúrate de que el script tenga permisos de ejecución:
```bash
chmod +x port_scan.py
```

## Uso
Ejecuta el script especificando el objetivo y los puertos:
```bash
python3 port_scan.py -t <objetivo> -p <puertos>
```

### Ejemplos
- Escanear un rango de puertos:
```bash
python3 port_scan.py -t 192.168.1.1 -p 1-1000
```
- Escanear puertos específicos:
```bash
python3 port_scan.py -t 192.168.1.1 -p 22,80,443
```

### Salida Esperada
- Si un puerto está abierto y responde, mostrará el encabezado HTTP:
```
[+] Puerto 80 abierto
HTTP/1.1 200 OK
...
```
- Si un puerto está abierto pero no responde, mostrará:
```
[-] Puerto 8080 abierto
```
- Si se presiona Ctrl+C durante la ejecución, se muestra:
```
[!] Saliendo...
```


