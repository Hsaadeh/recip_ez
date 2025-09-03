from django.urls import path
from . import views

view_urls = [
    path("", views.view_redirect, name="view_redirect"),
    path("page-not-found", views.view_not_found, name="view_not_found"),
]

api_urls = [
]

urlpatterns = view_urls + api_urls
