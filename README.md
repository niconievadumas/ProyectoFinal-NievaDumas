PROYECTO FINAL - CURSO DE PYTHON CODERHOUSE
AUTOR: NICOLAS NIEVA DUMAS

Este es un blog literario el cual permite la creacion de posteos de criticas literarias.
Nos permite la creacion, el listado, la modificacion y la eliminacion de posteos. Las ultimas dos acciones solo si estamos logueados.
Se puede registrar nuevos usuarios, editar los datos, modificar el password. Realizar logueos y deslogueos.
Contiene un link "acerca de" que contiene informacion del autor.
En el footer hay links funcionales que nos llegan al repositorio github de este proyecto, a una cuenta de twitter y el que esta en el medio con el logo de youtube nos lleva a un link de Loom donde esta el video solicitado.

Como extras la pagina de listado de posteos contiene una paginacion, estan ordenados cronologicamente de mas nuevo a mas antiguo.
Los posteos tienen como creador al usuario logueado y como fecha de creacion un datetime.now(). El titulo tiene formato title() y el sub y el contenido formato capitalize().