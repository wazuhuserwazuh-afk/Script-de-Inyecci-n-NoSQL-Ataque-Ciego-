# Script de Inyeccion NoSQL Ataque Ciego
Adapta el script para realizar tu ejercicio. 


Script de Inyección NoSQL (Ataque Ciego)

Este script de Python está diseñado con fines educativos para demostrar y explotar una vulnerabilidad de inyección NoSQL ciega. Es útil para retos de Capture The Flag (CTF) donde la respuesta del servidor no es explícita.
Características

    Altamente configurable: Usa argumentos de línea de comandos para la URL, usuario, cookies y encabezados.

    Detección doble: Utiliza el código de estado HTTP (302) o el tiempo de respuesta para detectar una inyección exitosa.

    Enfoque en CTFs: Intenta encontrar la contraseña carácter a carácter hasta que se completa.

Requisitos

Asegúrate de tener la librería requests instalada. Si no la tienes, puedes instalarla con pip:

pip install requests

Uso

El script requiere que le pases la URL de la página vulnerable y un nombre de usuario conocido. Los demás argumentos (cookies, encabezados, y el umbral de tiempo) son opcionales pero a menudo necesarios en los retos de CTF.
Sintaxis

python inyeccion_tiempo.py -u <URL> -user <USUARIO> [opciones]

Opciones importantes
Opción
Descripción
	
Ejemplo
-u, --url
	
(Obligatorio) URL completa de la página vulnerable.
	
-u "http://192.168.56.17/login.php"
-user
	
(Obligatorio) Nombre de usuario conocido en la base de datos.
	
-user "admin"
-c, --cookies
	
Cookies de la sesión en formato JSON.
	
-c '{"PHPSESSID": "abcdef123"}'
-H, --headers
	
Encabezados de la petición en formato JSON.
	
-H '{"Content-Type": "application/x-www-form-urlencoded"}'
-t, --threshold
	
Umbral de tiempo en segundos para la detección. Por defecto es 1.5.
	
-t 2.0
Ejemplo de uso completo

python inyeccion_tiempo.py \
    -u "[http://192.168.56.17/login.php](http://192.168.56.17/login.php)" \
    -user "admin" \
    -c '{"PHPSESSID": "0ff18974d13f43b3efb31"}' \
    -H '{"Host": "192.168.56.17", "User-Agent": "Mozilla/5.0", ...}'

¡Buena suerte con tus CTFs!
