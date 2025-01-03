from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.UserListView.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
     path('register/', views.register_user, name='register'),
]
