from django.db import models
from users.models import CustomUser

# Define class for Crop
class Crop(models.Model):
    name = models.CharField(max_length=100)
    growth_stage = models.CharField(max_length=50)
    health_status = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='crop_pics/', null=True, blank=True)
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Define class for Land
class Land(models.Model):
    size = models.FloatField()
    location = models.CharField(max_length=200)
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    crops = models.ManyToManyField(Crop)

    def __str__(self):
        return self.location