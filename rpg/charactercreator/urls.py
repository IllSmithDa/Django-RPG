from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.view_all_characters, name='characters'),
    path('character/([0-9]{1})/', views.view_character, name='character')
]
