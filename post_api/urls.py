from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.postAPIView, name='post-api'),
    path('post/<int:id>/', views.postDetailAPIView, name='post-details'),
    path('post/<int:id>/update/', views.postDetailUpdateAPIView, name='post-update'),
    path('post/<int:id>/delete/', views.postDeletePIView, name='post-delete'),
    path('users/', views.userAPIView, name='user-api'),
]