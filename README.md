# amigo-invisible
App para hacer el sorteo del amigo invisible

## Installation

Usar el package manager [pip](https://pip.pypa.io/en/stable/) para instalar detenv y poder usar las variables de entorno en ".env".

```bash
pip install python-dotenv
```
## Usage
Crear un .env con las siguientes vaiables:

```
EMAIL_USER=yourmail@gmail.com
EMAIL_PASSWORD=yourpassword
TXT_NAME=amigos.txt
```
Crea un txt llamado amigos.txt donde cada linea sea un participante, con la siguiente estructura: <nombre> <email>. Separados por un espacio.

Y finalmente activar el acceso de aplicaciones menos seguras para poder enviar mails de manera automatizada desde tu cuenta de gmail: https://myaccount.google.com/lesssecureapps
