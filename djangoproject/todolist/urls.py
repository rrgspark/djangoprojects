from django.urls import path, include
from . import views
urlpatterns = [ 
    path('main', views.main, name='main'),
    path('delete_item/<item_id>', views.delete_item, name='delete_item')
]