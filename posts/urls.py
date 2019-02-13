from django.urls import path

from posts import views


urlpatterns=[
    path('',views.PostsFeedView.as_view(),name="feed"),
    path('posts/new',views.create_post,name="create"),
]
