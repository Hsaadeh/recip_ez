from django.urls import path
from . import views

view_urls = [
    path("", views.view_home, name="view_home")
]

api_urls = [
]

urlpatterns = view_urls + api_urls
