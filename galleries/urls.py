from django.urls import path
from .views import gallery_list, gallery_details, add_gallery, add_photo

app_name = "galleries"
urlpatterns = [
    path('add_gal', add_gallery, name="add_gallery"),
    path('add_photo', add_photo, name="add_photo"),
    path('<int:gallery_id>', gallery_details, name='details'),
    path("", gallery_list, name="list"),

]