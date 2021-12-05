from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('moods/', views.moodPage, name="moods"),
    path('activities/', views.activitiesPage, name="activities"),
    path('logout/', views.logout_view, name='logout')
]