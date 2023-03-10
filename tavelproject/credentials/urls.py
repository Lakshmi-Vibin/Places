from django.urls import path, include

from credentials import views

urlpatterns = [
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
]
