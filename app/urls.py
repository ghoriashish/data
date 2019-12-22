from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.indexpage,name="indexpage"),
    path("registar",views.registarpage,name="registar"),
    path("show",views.show,name="show"),
    path("success",views.success,name="success")
]