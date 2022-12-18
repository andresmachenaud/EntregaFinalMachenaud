from django.shortcuts import render, redirect
from AppBlog.forms import *
from AppBlog.models import *
from AppLogin.forms import *
from AppLogin.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_request(request):

    if request.method == "POST":
        miFormulario = UserRegisterForm(request.POST)

        if miFormulario.is_valid():
            
            miFormulario.save()
            return redirect("login")
        else:
            return render(request, "AppLogin/registro.html", { "formulario": miFormulario, "errores": "Datos inválidos"})

    miFormulario  = UserRegisterForm()
    return render(request, "AppLogin/registro.html", { "formulario": miFormulario})

def confirmacion_registro(request):
    return render(request, "AppLogin/confirmacion_registro.html")

def login_request(request):
    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            login(request, user)
            return redirect("inicio")
        else:
            return render(request, "AppLogin/login.html", {"formulario": miFormulario, "errores": "Credenciales inválidas"})
    miFormulario = AuthenticationForm() #cuando crea el nuevo usuario le pasa al template un formulario vacío para que se vacíen los campos
    contexto = {"formulario": miFormulario}
    return render(request, "AppLogin/login.html", contexto)

@login_required
def editar_perfil(request,id):

    usuario = request.user
    perfil = Perfil.objects.get(user_id=usuario.id)
    if request.method == "POST" and "cargar-datos" in request.POST:
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.set_password(data["password1"])
            update_session_auth_hash(request, request.user) #al cambiar la contraseña mantengo la sesión iniciada
            usuario.save()
            return redirect("view-profile", id=usuario.username)
        else:
            return render(request, "AppLogin/profile.html",{"formulario": formulario, "errores": formulario.errors})
    if request.method == "POST" and "cargar-avatar" in request.POST:
        miFormulario_2 = AvatarForm(request.POST, files=request.FILES)
        if miFormulario_2.is_valid():
            #BORRO VIEJO AVATAR
            viejo_avatar = Avatar.objects.filter(user_id=usuario.id).order_by("-id")
            if viejo_avatar:
                viejo_avatar[0].delete()
            data_2 = miFormulario_2.cleaned_data
            avatar1 = Avatar(user=usuario, imagen=data_2["imagen"])
            avatar1.save()
            return redirect("view-profile", id=usuario.username)
        else:
            formulario = UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})
            return render(request, "AppLogin/profile.html", {"formulario": formulario,"formulario_2": AvatarForm(), "errores": miFormulario_2.errors })
    if request.method == "POST" and "cargar-datos-2" in request.POST:
        miFormulario_3 = PerfilEditForm(request.POST)
        if miFormulario_3.is_valid():
            data_3 = miFormulario_3.cleaned_data
            perfil.descripcion = data_3["descripcion"]
            perfil.link = data_3["link"]
            perfil.save()
            return redirect("view-profile", id=usuario.username)
        else:
            formulario = UserEditForm(initial = { "first_name": usuario.first_name, "last_name": usuario.last_name, "email": usuario.email})
            miFormulario_3 = PerfilEditForm(initial = {"descripcion": usuario.descripcion, "link": perfil.link})
            return render(request, "AppLogin/profile.html",{"formulario": formulario, "errores": miFormulario_3.errors})    
    formulario = UserEditForm(initial = { "first_name": usuario.first_name, "last_name": usuario.last_name, "email": usuario.email})
    miFormulario_3 = PerfilEditForm(initial = {"descripcion": perfil.descripcion, "link": perfil.link})
    return render(request, "AppLogin/profile.html", {"formulario":formulario,"formulario_2": AvatarForm(), "usuario": usuario, "formulario_3": miFormulario_3})

def ver_perfil(request,id):
    if not request.user.is_authenticated:
        return redirect("login")
    usuario=request.user
    perfil = Perfil.objects.get(user_id=usuario.id)
    avatares = Avatar.objects.filter(user_id=usuario.id).order_by("-id")
    if avatares:
        avatar_url=avatares[0].imagen.url
    else:
        avatar_url=""
    contexto = {"perfil": perfil,"avatar":avatar_url}
    return render(request, "AppLogin/view_profile.html",contexto)