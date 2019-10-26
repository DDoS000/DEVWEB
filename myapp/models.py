from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=1000)
    detail = models.CharField(max_length=1000)
    photo = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Contacts(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    mess = models.CharField(max_length=1000)
    time = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
