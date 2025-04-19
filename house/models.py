from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class House(models.Model):
    title = models.CharField(max_length=100)
    house_type = models.CharField(
        max_length=20, 
        choices=(
            ('Duplex', 'Duplex'),
            ('Bungalow', 'Bungalow')
        )
    )
    rent_price = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=50, 
        choices=(
            ('Abuja', 'Abuja'), 
            ('Lagos', 'Lagos'), 
            ('Rivers', 'Rivers')
        )
    )
    country = models.CharField(
        max_length=100, 
        choices=(
            ('Nigeria', 'Nigeria'),
        )
    )
    rent_cycle = models.CharField(
        max_length=50, 
        choices=(
            ('Monthly', 'Monthly'), 
            ('Yearly', 'Yearly')
        )
    )
    is_available = models.CharField(
        max_length=20, 
        choices=(
            ('Available', 'Available'), 
            ('Occupied', 'Occupied')
        )
    )
    landlord_notes = models.TextField(null=True)
    coo = models.FileField(upload_to='documents/') # certificate of occupancy 

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

class SaveHouse(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)

class HouseInspection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=40)
    inspection_date = models.DateField()

    created_on = models.DateTimeField(auto_now_add=True)

