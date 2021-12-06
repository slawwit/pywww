from django.urls import path
from .views import gallery_list

app_name = "galleries"
urlpatterns = [
    path("", gallery_list, name="list"),
]