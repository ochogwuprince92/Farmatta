from django.urls import path
from . import views

urlpatterns = [
    path('crops/', views.CropListCreateView.as_view(), name='crop-list-create'),
    path('crops/<int:pk>/', views.CropDetailView.as_view(), name='crop-detail'),
    path('lands/', views.LandListCreateView.as_view(), name='land-list-create'),
    path('lands/<int:pk>/', views.LandDetailView.as_view(), name='land-detail'),
]
