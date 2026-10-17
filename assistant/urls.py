from django.urls import path
from rest_framework.routers import DefaultRouter
from . import api


view_urls = []

api_urls = [
    path("api/agent-prompt/", api.api_agent_prompt, name="api_agent_prompt"),
]

urlpatterns = view_urls + api_urls
