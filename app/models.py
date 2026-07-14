from django.db import models

# Create your models here.
class Petshop(models.Model):
    pet_name=models.CharField(max_length=100)
    pet_image=models.ImageField(upload_to='pet_image/')
    def __str__(self):
        return self.pet_name
