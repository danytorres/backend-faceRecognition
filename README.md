# Notas para App Reconocimiento de emociones 

## Backend de Aplicación

Aplicacion backend corriendo en servidor de DigitalOcean en el dominio https://www.danytorresdev.tk/ 

Se pueden hacer la petición POST en /api/face/ para subir un formulario que contenga el nombre de la persona y la selfie para reconocimiento, la apicacion retorna un JSON con el nombre, donde se aloja la foto procesada dentro del servidor, y un arreglo de las 5 emociones con mas valor en la foto.

La logica de la peticion se encuentra en el archivo views.py en la carpeta endpoint.

La apicacion utiliza el Face API de microsoft, la logica se encuentra alojada en el archivo face.py en la carpeta endpoint.

Se utiliza un archivo mas que se llama emotions.py en la carpeta endpoint para poder hacer una logica para poder mostrar solo las 5 emociones con mas valor del arreglo entregado por la API de Microsoft.

Se puede correr la aplicacion en un contenedor desde el archivo docker-compose.yml que abrira el puerto 8000 local donde se puede hacer la peticion POST para subir la foto.