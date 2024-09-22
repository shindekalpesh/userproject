from django.urls import path, include
from homeapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/login', views.login, name='login'),
    path('/logout', views.logout, name='logout'),
]