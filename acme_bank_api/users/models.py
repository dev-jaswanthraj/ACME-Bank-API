from django.db import models
from django.conf import settings


class UserDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_details')
    street_address_1 = models.CharField(max_length=250)
    street_address_2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=50)
