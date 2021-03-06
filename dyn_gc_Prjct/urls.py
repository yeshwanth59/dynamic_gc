"""dyn_gc_Prjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from dyn_gc_App import views
from dyn_gc_App.views import Login
from django.conf.urls.static import static
from dyn_gc_App.middlewares.cant_login_after_login import cantLoginAfterLogin
from dyn_gc_App.middlewares.login_req_middleware import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^_nested_admin/', include('nested_admin.urls')),
    path("signup/", cantLoginAfterLogin(views.signup)),
    path("login/", cantLoginAfterLogin(Login.as_view())),
    path("home/", login_required(views.home)),
    path("logout/", views.logout),
    path("plot/", login_required(views.plot)),
    path("", views.srinfra),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
