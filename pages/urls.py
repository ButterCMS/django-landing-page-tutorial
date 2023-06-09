from django.urls import path

from . import views

urlpatterns = [
    path("", views.to_home, name="home"),
    path('<slug>', views.handler, name="handler"),
]