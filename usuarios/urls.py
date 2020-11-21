from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'usuarios' # usado na Django Template Language
urlpatterns = [
  path('', views.Lista.as_view(), name='lista'),
  path('criar', views.Criar.as_view(), name='usuario_criar'),
  path('<int:pk>', views.Visualizar.as_view(), name='usuario_vis'),
  path('<int:pk>/atualizar', views.Atualizar.as_view(), name='usuario_atualizar'),
  path('<int:pk>/deletar', views.Deletar.as_view(), name='usuario_del')
]