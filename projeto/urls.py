"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from projeto.portfolio.views import home, autocad, operador, curso_rapido, designer, dev_frontend, dev_games, \
    editor_videos, excel, profissionalizante, projetista, rotinas_adm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('autocad', autocad, name='autocad'),
    path('operador', operador, name='operador'),
    path('curso_rapido', curso_rapido, name='curso_rapido'),
    path('designer', designer, name='designer'),
    path('dev_frontend', dev_frontend, name='dev_frontend'),
    path('dev_games', dev_games, name='dev_games'),
    path('editor_videos', editor_videos, name='editor_videos'),
    path('excel', excel, name='excel'),
    path('profissionalizante', profissionalizante, name='profissionalizante'),
    path('projetista', projetista, name='projetista'),
    path('rotinas_adm', rotinas_adm, name='rotinas_adm'),
]
