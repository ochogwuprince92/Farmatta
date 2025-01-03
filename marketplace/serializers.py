from rest_framework import serializers
from .models import Listing, Transaction

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'crop', 'price', 'farmer']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'Listing', 'buyer', 'date', 'quantity']