from django.urls import path
from .views import posts_list, posts_details

app_name = "posts"
urlpatterns = [
    #path('<post_id>', posts_details),
    path('<int:post_id>', posts_details, name="details"),
    path('', posts_list, name="list"),
]