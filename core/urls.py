from django.urls import path
from . import views, home_view
app_name="core"

urlpatterns = [
    path('', views.home, name='home'),



    #dashboard Entreprise URLs private views
    path('dashboard/entreprises/', views.entreprise_list, name='entreprise_list'),
    path('dashboard/entreprises/<int:pk>/', views.entreprise_detail, name='entreprise_detail'),
    path('entreprises/create/', views.entreprise_create, name='entreprise_create'),
    path('dashboard/entreprises/<int:pk>/update/', views.entreprise_update, name='entreprise_update'),
    # path('entreprises/<int:pk>/archive/', views.entreprise_archive, name='entreprise_archive'),

    #address entreprise URLs private views
    path('dashboard/entreprises/<int:pk>/add_address/', views.add_address_entreprise, name='add_address_entreprise'),


    #contact entreprise URLs private views
    path('dashboard/entreprises/<int:pk>/contacts/', views.contact_list, name='contact_list'),
    path('dashboard/entreprises/<int:pk>/add_contact/', views.add_contact_entreprise, name='add_contact_entreprise'),

    #contenu entreprise URLs private views
    path('dashboard/entreprises/<int:pk>/add_contenus/', views.add_contenu_entreprise, name='contenu_add'),
    path('dashboard/entreprises/<int:pk>/contenus/', views.list_contenu_entreprise, name='list_contenu_entreprise'),



    #public view
    path('entreprises/', home_view.list_entreprise, name='list_entreprise_public'),
    path('entreprise/detail/<int:pk>/', home_view.entreprise_detail_public, name='entreprise_detail_public'),
]