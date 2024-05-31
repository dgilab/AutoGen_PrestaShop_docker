# Auto Generador Compose PrestaShop

Este generador utiliza Docker Compose para orquestar un conjunto de contenedores que incluyen servicios como phpMyAdmin, PrestaShop.

## Dependencias

Debes tener instalado python

## Instalación

Principalmente es necesario tener instalado Docker en su sistema.

Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```
Esto instalará las bibliotecas Python necesarias para ejecutar el script.

## Uso

Una vez que hayas instalado las dependencias, ejecuta el siguiente comando para iniciar el script desde la terminal:

```bash
python generador_compose.py
```

El script solicitará los datos necesarios, como los nombres de los contenedores, las variables de entorno y los nombres de host. Una vez que hayas proporcionado esta información, se generará un archivo docker-compose.yml personalizado y se iniciará Docker Compose.

## Auto Generador Wordpress

Si quiere generar un compose para Wordpress, accede al siguiente enlace: [WordpressGitHub](https://github.com/dgilab/AutoGen_WordPress_docker)
