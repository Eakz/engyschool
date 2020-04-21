from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.post_create, name='post_create'),
    path('post/<int:post_id>', views.post_edit, name='post_edit'),
    path('about-us/',views.about, name='about'),
]