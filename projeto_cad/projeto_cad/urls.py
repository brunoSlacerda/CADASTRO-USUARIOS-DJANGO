

from django.urls import path
from app_cad import views   

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem')
]
