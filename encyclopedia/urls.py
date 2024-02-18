from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.article, name="article"),
    path("add", views.add, name="add"),
    path("404", views.not_found, name="404")
]
