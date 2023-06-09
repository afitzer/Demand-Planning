from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('planning/', views.planning, name='planning'),
    path('reports/', views.reports, name='reports'),
    path('game/', views.game, name='game'),
]