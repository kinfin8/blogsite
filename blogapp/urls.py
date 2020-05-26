from django.urls import path

from . import views

app_name = 'blogapp'

urlpatterns = [
    # ex: blog/
    path('', views.display_index, name='display_index'),
    # ex: blog/post/post_url/
    path('post/<str:post_url>/', views.display_post, name='display_post'),
]
