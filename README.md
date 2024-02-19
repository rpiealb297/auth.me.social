# Me.Social

Aquí tenemos la API de autentificación de la aplicación me.social. 

## Despliegue de la API

Este documento proporciona instrucciones detalladas sobre cómo desplegar y ejecutar la API en diferentes entornos, incluyendo Docker, si es necesario.

### Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Docker

### Despliegue con Docker

Para desplegar la API usando Docker, sigue estos pasos:

1. **Construir la Imagen Docker:**

   La imagen Docker deberá de estar basada en `python:3.9-slim`, ya que utilizamos Python 3.9, cuando crees tu imagen, asegurate de que te encuentras en el directorio raíz de tu proyecto (donde se encuentra tu `Dockerfile`):

2. **Directorio de trabajo:**
   
   El directorio de trabajo de este servicio será `/app`, para ello deberás de utilizar el comando 
   ```bash
   WORKDIR /app

3. **Copia de ficheros:**

   Los archivos de la API deben estar en `/app` dentro del contenedor. Asegúrate de que tu `Dockerfile` esté configurado para copiar los archivos del proyecto a esta ubicación.

4. **Ejecución del fichero:**

    Para ejecutar el fichero, hay que utilizar el comando `python main.py` adapta tu Dockerfile para garantizar que ejecute este fichero y el contenedor queda ejecutándose en segundo plano.

4. **Nombre del contenedor:**

   Se recomienda que el nombre del docker creado sea `me-social-auth`

## Endpoints

La API expone los siguientes endpoints:

- `http://<docker-ip>/login`: Recibe un json vía POST del estilo `{"user":"USUARIO", "passw":"CONTRASEÑA"}` y devuelve un json donde informa si se ha completado o no el login realizado.

## Recomendaciones de despliegue

Recuerda que esta API está enlazada con la aplicación `me.social`. Desde esta aplicación web, se realizan llamadas de tipo GET hasta esta api utilizando una URL de este tipo: 
- `http://me.social/login` 

Si estás utilizando Apache, recuerda configurar el sistema para que se pueda acceder utilizando esta URL. No debes de cambiar en ningún momento el código fuente

## Autentificación

En este caso, el usuario será: `mortadelo` y la contraseña: `filemon`

## Pruebas
Para hacer las pruebas, utiliza un `POSTMAN` realiza una petición `POST` con `http://me.social/login` y en el body, utilizando raw, utiliza el JSON con el usuario y contraseña adecuado.
