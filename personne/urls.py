from django.urls import path
from . import views


app_name='personne'

urlpatterns = [
    path('',views.home,name='home'),
    path('add_docteur',views.add_docteur,name='add_docteur'),
    path('list_docteur',views.list_docteur,name='list_docteur'),
    path('list_personne',views.list_personne,name='list_personne'),
]