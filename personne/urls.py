from django.urls import path
from . import views


app_name='personne'

urlpatterns = [
    path('',views.home,name='home'),
    #ajouter
    path('add_docteur',views.add_docteur,name='add_docteur'),
    path('add_hospitialiser',views.add_hospitialiser,name='add_hospitialiser'),
    path('add_infermier',views.add_infermiere,name='add_infermier'),
    path('add_maladie',views.add_maladie,name='add_maladie'),
    path('add_salle',views.add_salle,name='add_salle'),
    path('add_service',views.add_service,name='add_service'),
    path('add_specialite',views.add_specialite,name='add_specialite'),

    #Delete
    path('delete_docteur/<int:docteur_id>/delete', views.DocteurDeleteView, name='delete_docteur'),
    path('delete_hopitialiser/<int:docteur_id>/delete', views.HospitialiserDeleteView, name='delete_hospitialiser'),
    path('delete_infermier/<int:docteur_id>/delete', views.InfermierDeleteView, name='delete_infermier'),
    path('delete_maladie/<int:docteur_id>/delete', views.MaladieDeleteView, name='delete_maladie'),
    path('delete_salle/<int:docteur_id>/delete', views.SalleDeleteView, name='delete_salle'),
    path('delete_service/<int:docteur_id>/delete', views.ServiceDeleteView, name='delete_service'),
    path('delete_specialite/<int:docteur_id>/delete', views.SpecialiteDeleteView, name='delete_specialite'),


    #Update
    path('update_docteur/<int:docteur_id>/update', views.DocteurUpdate, name='update_docteur'),
    path('update_hopitialiser/<int:docteur_id>/update', views.HospitaliserUpdate, name='update_hospitialiser'),
    path('update_infermier/<int:docteur_id>/update', views.InfermierUpdate, name='update_infermier'),
    path('update_maladie/<int:docteur_id>/update', views.MaladieUpdate, name='update_maladie'),
    path('update_salle/<int:docteur_id>/update', views.SalleUpdate, name='update_salle'),
    path('update_service/<int:docteur_id>/update', views.ServiceUpdate, name='update_service'),
    path('update_specialite/<int:docteur_id>/update', views.SpecialiteUpdate, name='update_specialite'),

    #liste
    path('list_docteur',views.list_docteur,name='list_docteur'),
    path('list_hospitialiser',views.list_hospitialiser,name='list_hospitialiser'),
    path('list_infermier',views.list_infermier,name='list_infermier'),
    path('list_maladie',views.list_maladie,name='list_maladie'),
    path('list_salle_specialite',views.list_salle_specialite,name='list_salle_specialite'),
    path('list_service',views.list_service,name='list_service'),
    path('list_personne',views.list_personne,name='list_personne'),

    #datail
    path('detail_docteur/<int:docteur_id>/detail/', views.DocteurDetail, name='detail_docteur'),
    path('detail_service/<int:service_id>/detail/', views.ServiceDetail, name='detail_service'),
    path('detail_maladie/<int:maladie_id>/detail/', views.MaladieDetail, name='detail_maladie'),
]