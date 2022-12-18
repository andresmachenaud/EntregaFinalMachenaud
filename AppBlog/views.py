from django.shortcuts import render, redirect, HttpResponse
from AppBlog.forms import *
from AppBlog.models import *
from AppLogin.forms import *
from AppLogin.models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

def base(request):
    return render(request, "AppBlog/base.html")

def inicio(request):
    entradas = Entrada.objects.all().order_by("-id")
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")
        if imagen_model:
            imagen_url = imagen_model[0].imagen.url
        else:
            imagen_url = ""
    else:
        imagen_url = ""
    categorias = []
    for entrada in entradas:
        if entrada.libro.categoria not in categorias:
            categorias.append(entrada.libro.categoria)
    return render(request, "AppBlog/index.html", {"imagen_url": imagen_url, "listado_entradas": entradas[0:3],"categorias": categorias,"listado_entradas_total": entradas})

def about(request):
    return render(request, "AppBlog/about.html",)

def blog(request):
    entradas = Entrada.objects.all().order_by("-id")
    categorias = []
    for entrada in entradas:
        if entrada.libro.categoria not in categorias:
            categorias.append(entrada.libro.categoria)
    contexto = {"listado_entradas": entradas, "categorias": categorias,"listado_entradas_recientes":entradas[0:3]}
    return render(request, "AppBlog/pages.html", contexto) 

def libros(request):
    libros = Libro.objects.all()
    entradas = Entrada.objects.all().order_by("-id")
    categorias = []
    for entrada in entradas:
        if entrada.libro.categoria not in categorias:
            categorias.append(entrada.libro.categoria)
    contexto = {"listado_entradas": entradas, "categorias": categorias,"listado_libros": libros,"listado_entradas_recientes":entradas[0:3]}
    if request.user.is_superuser:
        contexto["is_superuser"]=1
    return render(request, "AppBlog/libros.html", contexto)

def crear_entrada(request):
    errores=""
    #Validamos tipo de petición
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        #Cargamos los datos en el formulario
        miFormulario = EntradaFormulario(request.POST, request.FILES)
        #Validamos los datos:
        if miFormulario.is_valid():
            #Recuperamos los datos limpios:
            data = miFormulario.cleaned_data
            #Creamos el curso
            miEntrada = Entrada(
            titulo=data["titulo"],
            subtitulo=data["subtitulo"],
            autor=Perfil.objects.get(user_id= request.user.id),
            fecha=datetime.now(),
            libro=data["libro"],
            calificacion=data["calificacion"],
            cuerpo=data["cuerpo"],
            imagen=data["imagen"])
            miEntrada.save()
        else:
            return render(request, "AppBlog/crear_entrada.html",{"formulario": miFormulario, "errores": miFormulario.errors})
    miFormulario = EntradaFormulario()
    contexto = {"formulario": miFormulario, "errores": errores}
    return render(request, "AppBlog/crear_entrada.html", contexto) 

@login_required
def editar_entrada(request,id):
    entrada = Entrada.objects.get(id=id)
    if request.method == "POST":
        if request.user == entrada.autor.user:
            miFormulario = EditarEntradaFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                entrada.titulo = data["titulo"]
                entrada.subtitulo = data["subtitulo"]
                entrada.calificacion = data["calificacion"]
                entrada.cuerpo = data["cuerpo"]
                if data["imagen"]:
                    entrada.imagen = data["imagen"]
                entrada.save()
                return redirect("page-details",id)
            else:
                return render(request, "AppBlog/editar_entrada.html",{"formulario": miFormulario, "errores": miFormulario.errors})
    else:
        miFormulario = EditarEntradaFormulario(initial={"titulo": entrada.titulo, "subtitulo": entrada.subtitulo,"libro": entrada.libro, "calificacion": entrada.calificacion, "cuerpo": entrada.cuerpo, "imagen": entrada.imagen})
        return render(request, "AppBlog/editar_entrada.html",{"formulario": miFormulario, "errores": ""})

def buscar_entrada(request):
    titulo_entrada = request.GET["titulo_entrada"]
    listado_entradas = Entrada.objects.filter(titulo__icontains=titulo_entrada)
    entradas = Entrada.objects.all().order_by("-id")
    categorias = []
    for entrada in entradas:
        if entrada.libro.categoria not in categorias:
            categorias.append(entrada.libro.categoria)
    contexto = {"listado_entradas_total": entradas, "categorias": categorias,"listado_entradas": listado_entradas, "listado_entradas_total":entradas, "listado_entradas_recientes":entradas[0:3]}
    return render(request, "AppBlog/busqueda_entrada.html", contexto)

def buscar_entrada_cat(request,cat):
    cat_libro = cat
    libros = Libro.objects.filter(categoria__icontains=cat_libro)
    entradas= Entrada.objects.all()
    listado_entradas=[]
    categorias = []
    for entrada in entradas:
        if entrada.libro in libros:
            listado_entradas.append(entrada)
    for entrada in entradas:
        if entrada.libro.categoria not in categorias:
            categorias.append(entrada.libro.categoria)
    contexto = {"listado_entradas_total": entradas, "categorias": categorias,"listado_entradas": listado_entradas}
    return render(request, "AppBlog/busqueda_entrada.html", contexto)

def buscar_entrada_libro(request,lib):
    listado_entradas= Entrada.objects.filter(libro_id=lib)
    categorias = []    
    entradas= Entrada.objects.all()
    for entrada in entradas:
        if entrada.libro.categoria not in categorias:
            categorias.append(entrada.libro.categoria)
    contexto = {"listado_entradas_total": entradas, "categorias": categorias,"listado_entradas": listado_entradas}
    return render(request, "AppBlog/busqueda_entrada.html", contexto)

def eliminar_entrada(request, id):
    entrada = Entrada.objects.get(id=id) #no usamos método filter porque devuelve una lista y solo quiero un objeto
    entrada.delete()
    return redirect("inicio")

def cargar_libro(request):
    categorias = ["Categoría","Arte", "Biografía","Negocios","Infantil","Comics","Cocina","Fantasía","Ficción","Novela gráfica","Ficción histórica","Ciencia Ficción","Autoayuda","Deportes","Suspenso","Turismo","Juvenil","Terror"]
    errores=""
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            miLibro = Libro(
            titulo=data["titulo"],
            autor=data["autor"],
            ano=data["ano"],
            categoria=data["categoria"],
            editorial=data["editorial"])
            miLibro.save()
        else:
            errores = miFormulario.errors
    miFormulario = LibroFormulario()
    contexto = {"formulario": miFormulario, "errores": errores, "categorias":categorias}
    return render(request, "AppBlog/cargar_libro.html", contexto)

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id) #no usamos método filter porque devuelve una lista y solo quiero un objeto
    libro.delete()
    return redirect("login")

def detalle_entrada(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    entradas_o = Entrada.objects.all().order_by("-id")
    entrada = Entrada.objects.get(id=id)
    imagen_url = entrada.imagen.url
    comentarios = Comentario.objects.filter(post_id=id).order_by("-fecha")
    num_comentarios = comentarios.count()
    categorias = []
    for i in entradas_o:
        if i.libro.categoria not in categorias:
            categorias.append(i.libro.categoria)
    query = list()
    for comentario in comentarios:
        avatar=comentario.get_avatar()
        if avatar:
            query.append((comentario,avatar))
        else:
            query.append((comentario,""))
    errores=""
    if request.method == "POST":
        miFormulario = ComentarioFormulario(request.POST)
        perfil=Perfil.objects.get(user_id=request.user.id)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            miComentario = Comentario(autor=perfil,
            cuerpo=data["cuerpo"], post=entrada)
            miComentario.save()
            return redirect("page-details", id=id)
        else:
            errores = miFormulario.errors
    miFormulario = ComentarioFormulario() 
    contexto = {"entrada": entrada, "imagen_url": imagen_url, "comentarios": comentarios, "num_comentarios": num_comentarios,"listado_entradas": entradas_o[0:3],"categorias": categorias,"listado_comentarios_avatars": query, "formulario": miFormulario, "errores": errores}
    return render(request, "AppBlog/post-details.html", contexto)

def contact(request):
    return render(request, "AppBlog/contact.html",)

def comunidad(request):
    if not request.user.is_authenticated:
        return redirect("login")
    errores=""
    if request.method == "POST":
        miFormulario = MensajeFormulario(request.POST)
        perfil=Perfil.objects.get(user_id=request.user.id)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            miMensaje = Mensaje(autor=perfil,
            cuerpo=data["cuerpo"])
            miMensaje.save()
            return redirect("comunidad")
        else:
            errores = miFormulario.errors
    mensajes = Mensaje.objects.filter().order_by("-fecha")
    query = list()
    miFormulario = MensajeFormulario() 
    for mensaje in mensajes:
        avatar=mensaje.get_avatar()
        if avatar:
            query.append((mensaje,avatar))
        else:
            query.append((mensaje,""))
    contexto = {"listado_mensajes": query, "formulario": miFormulario, "errores": errores}
    return render(request, "AppBlog/comunidad.html", contexto) 
