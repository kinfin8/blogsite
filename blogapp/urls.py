from django.urls import path

from . import views

app_name = 'blogapp'

urlpatterns = [
    # ex: /
    path('', views.display_index, name='display_index'),
    # ex: archive/
    path('archive/', views.display_archive, name='display_archive'),
    # ex: about/
    path('about/', views.display_about, name='display_about'),
    # ex: post/post_url/
    path('post/<str:post_url>/', views.display_post, name='display_post'),
]
