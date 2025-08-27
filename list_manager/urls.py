from django.urls import path
from . import views


view_urls = [
    path("shopping-lists", views.view_shopping_lists, name="view_shopping_lists"),
    path("shopping-list/<int:id>", views.view_shopping_list, name="view_shopping_list"),
]

api_urls = [
]

urlpatterns = view_urls + api_urls
