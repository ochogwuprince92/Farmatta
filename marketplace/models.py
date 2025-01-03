from django.db import models
from users.models import CustomUser
from farm_management.models import Crop

# Define class for Listing
class Listing(models.Model):
    Crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Listing for {self.crop.name}"

# Define a class for Transaction
class Transaction(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Transaction for {self.listing.crop.name} by {self.buyer.username}"
    
