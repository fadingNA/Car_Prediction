from django.db import models

# Create your models here.
class uploaded(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    year = models.IntegerField()
    kms_driven = models.FloatField()
    fuel_type = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
class Route(models.Model):
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    distance = models.FloatField()
    time = models.FloatField()
    fuel_price = models.FloatField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Route start {self.start} to end {self.end} by {self.car.name}"