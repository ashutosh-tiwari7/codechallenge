from django.db import models

class Apartments(models.Model):
    name = models.CharField(max_length=100)
    rent = models.CharField(max_length=100)
    rooms = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name