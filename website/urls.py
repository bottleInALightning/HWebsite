from django.urls import path

from . import views

urlpatterns = [
    
    path("",views.homepage),
    path("create_room",views.create_room)
    ]