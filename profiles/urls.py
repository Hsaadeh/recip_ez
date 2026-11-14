from django.urls import path
from . import views, api

view_urls = [
    path("", views.view_redirect, name="view_redirect"),
    path("sign-in/", views.view_sign_in, name="view_sign_in"),
    path("logout/", views.view_logout, name="view_logout"),
    path("page-not-found", views.view_not_found, name="view_not_found"),
]

api_urls = [
    path("api/sign-in/", api.api_sign_in, name="api_sign_in")
]

urlpatterns = view_urls + api_urls
