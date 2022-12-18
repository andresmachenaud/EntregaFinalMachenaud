from django.urls import path
from AppBlog.views import *
from AppLogin.views import *
from django.contrib.auth.views import LogoutView
import EntregaFinalMachenaud.settings as settings
from django.conf.urls.static import static

urlpatterns = [ 
    path("accounts/login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(template_name="AppLogin/logout.html"), name="logout"),
    path("registro/", register_request, name="registro"),
    path("accounts/profile/edit/<id>", editar_perfil, name="profile"),
    path("accounts/profile/<id>", ver_perfil, name="view-profile")
]

# Agregar las URLS de archivos estaticos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)