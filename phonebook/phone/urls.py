from django.urls import path
from .views import home,add_name,remove_name

urlpatterns = [
    path("",home,name="home"),
    path("add/<str:name>/<int:number>/",add_name, name="add"),
    path("dell/<str:name>/" , remove_name, name = "del"),
]
