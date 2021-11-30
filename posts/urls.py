from django.urls import path
from .views import posts_list, posts_details, add_post, edit_post

app_name = "posts"
urlpatterns = [
    # path('<post_id>', posts_details),
    path('add', add_post, name="add"),
    path('<int:post_id>', posts_details, name="details"),
    path('<int:post_id>/edit', edit_post, name='edit'),
    path('', posts_list, name="list"),

]
