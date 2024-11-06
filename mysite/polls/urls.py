from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('consulta/', views.consulta_view, name='consulta'),
    path('documentacao/', views.documentacao_view, name='documentacao'),
    path('curiosidades/', views.curiosidades_view, name='curiosidades'),
]
