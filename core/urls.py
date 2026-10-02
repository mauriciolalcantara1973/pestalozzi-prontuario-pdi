from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('atendimento/', views.atendimento, name='atendimento'),
    path('historico/', views.historico, name='historico'),
]
