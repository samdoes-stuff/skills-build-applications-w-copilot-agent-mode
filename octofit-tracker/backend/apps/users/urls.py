from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfileList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserProfileDetail.as_view(), name='user-detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
]