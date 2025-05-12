"""

Trabajo Practico 2 - Git y GitHub

1) Contestar las siguientes preguntas utilizando las guías y documentación proporcionada 
(Desarrollar las respuestas) :   
• ¿Qué es GitHub?

	GitHub es una plataforma de desarrollo colaborativo basada en Git que permite a los desarrolladores alojar, revisar y gestionar 	proyectos de software de manera distribuida. Es ampliamente utilizada para el control de versiones y el trabajo en equipo, 	facilitando la colaboración tanto en proyectos open source como privados.

• ¿Cómo crear un repositorio en GitHub?  

	Para crear un repositorio en GitHub se hacen los siguientes pasos: se inicia sesión con una cuenta de GitHub, se da click en "+" y 	en la opción "New Repository", se ingresa un nombre para el repositorio, una descripción opcional y se elige si sera publico o 	privado

• ¿Cómo crear una rama en Git?
	
	Para crear una rama en Git, se escribe el comando git branch seguido del nombre de la rama. Por ejemplo: 
	git branch nueva-rama
  
• ¿Cómo cambiar a una rama en Git?

	Para cambiar a una rama en Git, se usa el comando git checkout seguido del nombre de la rama. Por ejemplo: 
	git checkout nueva-rama
  
• ¿Cómo fusionar ramas en Git?  

	Para fusionar ramas en Git, primero debemos situarnos en la rama que va a contener los cambios, luego usamos el comando git merge 	seguido del nombre de la rama. Por ejemplo: 
	git checkout rama-1
	git merge rama-2

• ¿Cómo crear un commit en Git?  

	Para crear un commit en Git, primero se añaden los archivos al area de preparación con el comando git add, seguido del comando git 	commit y un mensaje descriptivo del commit. Por ejemplo: 
	git add .
	git commit -m "Mensaje"

• ¿Cómo enviar un commit a GitHub?  
	
	Para enviar un commit a GitHub, se usa el comando git push seguido del nombre de la rama y del repositorio remoto. Por ejemplo: 
	git push origin master

• ¿Qué es un repositorio remoto?  
	
	Un repositorio remoto de Git es una version del proyecto almacenada en un servidor en linea o en otra ubicación remota

• ¿Cómo agregar un repositorio remoto a Git?  
	
	Para agregar un repositorio remoto a Git, se usa el comando git remote add seguido del nombre y la URL del repositorio remoto. por 	ejemplo: 
	git remote add origin URL-del-repositorio

• ¿Cómo empujar cambios a un repositorio remoto?  

	Para empujar cambios en un repositorio remoto de Git, se usa el comando git push seguido del nombre del repositorio y la rama.
	Por ejemplo: 
	git push origin main

• ¿Cómo tirar de cambios de un repositorio remoto?  

	Para traer cambios de un repositorio remoto a uno local, se usa el comando git pull seguido del nombre del repositorio y la rama.
	Por ejemplo:
	git pull origin main

• ¿Qué es un fork de repositorio?  

	Un fork de repositorio en GitHub es una copia de un repositorio ajeno a la cuenta de usuario. Permite trabajar en modificaciones 	sin afectar el repositorio original hasta que se envíen como pull request

• ¿Cómo crear un fork de un repositorio?  

	Para crear un fork debemos situarnos en el repositorio original y hacer click en el botón "Fork". Luego añadir un nombre y una 	descripción opcional y por ultimo dar click en el botón "Create fork"

• ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?  

	Para hacer un pull request hay que crear una rama en el repositorio local, crear los commits, empujar la rama en el fork y en 	GitHub habrá un mensaje indicando que se empujo una nueva rama. Hacemos clic en "Compare & pull request", se escribe un titulo y 	una descripción de los cambios y nos aseguramos de comparar la rama base del repositorio con la nueva rama. Por ultimo se da click 	en "Create pull request"
	
• ¿Cómo aceptar una solicitud de extracción?  

	En el repositorio original debemos ir a la pestaña "Pull request", dar click en la solicitud a revisar, y si los cambios son 	correctos se hace click en "Merge pull request" y "Confirm merge"

• ¿Qué es un etiqueta en Git?  

	Una etiqueta en Git es una referencia a un punto específico en la historia del repositorio, como versiones estables o lanzamientos 	importantes

• ¿Cómo crear una etiqueta en Git?  

	Para crear una etiqueta en Git, utiliza git tag seguido del nombre de la etiqueta y opcionalmente el hash del commit. 
	Por ejemplo:	
	git tag -a v1.0 -m "Version 1.0"

• ¿Cómo enviar una etiqueta a GitHub?  

	Para enviar una etiqueta a GitHub, se usa el comando git push seguido de --tag. Por ejemplo:
	git push origin --tag

• ¿Qué es un historial de Git?  

	El historial de Git es el registro de todos los cambios realizados en un repositorio, incluyendo commits, fusiones y etiquetas

• ¿Cómo ver el historial de Git?  

	Para ver el historial de Gis se usa el comando git log

• ¿Cómo buscar en el historial de Git?

	Con el comando git log --online podemos ver cada commit en una sola linea y con el comando git log --graph podemos ver un grafico 	ASCII con ramas y merges  

• ¿Cómo borrar el historial de Git?  

	Para borrar el historial de Git debemos crear un nuevo commit con el estado actual del proyecto: 

	rm -rf .git
	git init
	git add .
	git commit -m "Reinicio del historial"

	Ahora se vuelve a agregar el repositorio remoto:

	git remote add origin https://github.com/usuario/repositorio.git
	git push -f origin main

• ¿Qué es un repositorio privado en GitHub?  

	Un repositorio privado en GitHub es un repositorio que solo puede ser visto y contribuido por usuarios autorizados

• ¿Cómo crear un repositorio privado en GitHub?  

	Para crear un repositorio privado hacemos click en "+", "New repository" y marcamos la opción "Private"
 
• ¿Cómo invitar a alguien a un repositorio privado en GitHub?  

	Para invitar a alguien a colaborar en un repositorio privado en GitHub, vamos a la página del repositorio, hacemos clic en "	Settings", luego en "Manage access" y agrega el nombre de usuario del colaborador

• ¿Qué es un repositorio público en GitHub?  

	Un repositorio público en GitHub es aquel que es visible y accesible para cualquier usuario de GitHub

• ¿Cómo crear un repositorio público en GitHub?  

	Para crear un repositorio publico hacemos click en "+", "New repository" y marcamos la opción "Public"

• ¿Cómo compartir un repositorio público en GitHub? 

	Para compartir un repositorio publico debemos compartir la URL del mismo

"""