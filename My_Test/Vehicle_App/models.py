from django.db import models

class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    mileage = models.FloatField()
    v_type = models.CharField(max_length=50)
    seats = models.IntegerField()
    v_seat_type = models.CharField(max_length=50)
    owner = models.CharField(max_length=100)
    o_contact = models.BigIntegerField()
    feedback = models.TextField()
