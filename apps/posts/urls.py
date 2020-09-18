from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    
    path('lista/', views.Post_list, name='post_list'),
    path('<int:pk>/', views.Post_detail, name='post_detail'),
     path('new/', views.Post_new, name='post_new'),
   ]
