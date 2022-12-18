# EntregaFinalMachenaud

Creado por Andrés Machenaud

El siguiente proyecto consiste en la creación de una página web tipo Blog para reviews de libros. Para ello los usuarios pueden cargar
un libro y luego asociarlo a un post. Las únicas personas que pueden eliminar un post son los creadores o los superusuarios.

Solo los superusuarios pueden borrar los libros cargados a la página.

Hay un buscador de entradas al blog.

Se pueden cargar comentarios en la vista detallada de los posts, y en la sección comunidad enviar mensajes entre los usuarios.

El modelo tiene las clases:
Libro: Título, autor, categoría, editorial, año de publicación
Entrada: Título, subitítulo, autor, fecha creación, fecha edición, libro, calificación, cuerpo, imagen
Comentario, Autor, fecha, cuerpo
Perfil: Usuario, descripción, link
Avatar: usuario, imagen

Paquetes instalados:
pip install django-ckeditor

Todos los usuarios tienen contraseña: bestreads

superuser: usuario
clave: bestreads