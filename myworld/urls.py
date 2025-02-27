from django.urls import path
from .views import toggle_message

urlpatterns = [
    path("toggle/", toggle_message, name="toggle_message"),
]
