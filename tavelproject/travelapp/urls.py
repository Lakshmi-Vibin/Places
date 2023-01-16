from .import views
from django.urls import path

urlpatterns = [

    # path('',views.demo, name='demo'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about')

]