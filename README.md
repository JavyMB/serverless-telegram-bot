## Serverless Telegram bot en AWS Lambda

### Intro
Este es un template sencillo para regresar un eco del mesaje escrito en Telegram, usando Python3 y lanzar en AWS Lamda usuando Serverless framework.

Puedes encontrar el tutorial completo en Iglés [aquí](https://medium.com/@andriidvoiak/serverless-telegram-bot-on-aws-lambda-851204d4236c)

### Requerimientos
 1. Python 3
 2. Node.js v6.5.0 o anterior
 3. Cuenta deAWS  con permisos Administrador

### Deploying 

Instala el "framework" llamado "erverless":

`npm install -g serverless`

Exporta tus credenciales:

```
export AWS_ACCESS_KEY_ID=<Access key ID>
export AWS_SECRET_ACCESS_KEY=<Secret access key>
export TELEGRAM_TOKEN=<Your Telegram Token>
```

Instala los requerimientos pip :

`pip install -r requirements.txt -t vendored`

Sube a AWS:

`serverless deploy`
