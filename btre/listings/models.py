from django.db import models
from datetime import datetime
# from realtors.models import Realtor
# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    desciption = models.TextField(blank=True)
    # Overview = models.TextField(blank=True)
    # content = models.TextField(blank=True)
    # table = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    content = models.TextField(blank=True)
    table = models.TextField(blank=True)



    price = models.IntegerField()



    bedrooms = models.IntegerField()
    # bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garaze = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
