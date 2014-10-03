from django.db import models


class Contact(models.Model):
    given_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=200, blank=True)
    email_address = models.EmailField(blank=True)
    telephone_number = models.CharField(max_length=200, blank=True)
