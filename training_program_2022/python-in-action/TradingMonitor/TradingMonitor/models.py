from sqlite3 import Timestamp
from django.db import models
from django.forms import CharField


class Position(models.Model):
    asset = models.CharField(max_length=10)
    Timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
