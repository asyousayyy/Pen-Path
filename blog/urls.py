from django.urls import path

from .views import post_list, post_detail,post_create

urlpatterns = [
    path("",post_list,name="post-list"),
    path("post/<int:post_id>" , post_detail ,name="post-detail"),
    path("create/", post_create, name="post-create"),
]
