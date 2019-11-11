from django.urls import path, include
from . import views
urlpatterns = [
    path('',include('django.contrib.auth.urls')), 
    path('logout', views.logout, name="logout"), 
    path('main', views.main, name='main'),
    path('registrar', views.registrar, name="registrar")
]