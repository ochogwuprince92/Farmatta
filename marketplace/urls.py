from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.ListingListCreateView.as_view(), name='listing-list-create'),
    path('listings/<int:pk>', views.ListingDetailView.as_view(), name='listing-detail'),
    path('transaction/', views.TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transaction/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),    
]
