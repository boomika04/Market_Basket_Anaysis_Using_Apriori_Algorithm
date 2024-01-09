from django.db import models

# Create your models here.
from django.db import models

class Transaction(models.Model):
    items = models.TextField()
