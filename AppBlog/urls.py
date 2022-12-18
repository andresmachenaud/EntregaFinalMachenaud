from django.urls import path
from AppBlog.views import *
from AppLogin.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("about/", about, name="about"),
    path("libros/", libros, name="libros"),
    path("pages/crear/", crear_entrada, name="pages-crear"),
    path("pages/", blog, name="pages"),
    path("libro/crear/", cargar_libro, name="libro-cargar"),
    path("libro/borrar/<id>", eliminar_libro, name="libro-borrar"),
    path("pages/<id>", detalle_entrada, name="page-details"),
    path("pages/editar/<id>", editar_entrada, name="page-edit"),
    path("pages/search/", buscar_entrada, name="page-search"),
    path("pages/search/cat/<cat>/", buscar_entrada_cat, name="page-search-cat"),
    path("pages/search/libro/<lib>/", buscar_entrada_libro, name="page-search-libro"),
    path("pages/borrar/<id>", eliminar_entrada, name="page-borrar"),
    path("messages/", comunidad, name="comunidad"),
]