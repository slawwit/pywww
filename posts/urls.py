from django.urls import path
from .views import posts_list, posts_details

urlpatterns = [
    path('', posts_list),
    path('1', posts_details),
]