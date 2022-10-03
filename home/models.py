from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Activity_List(models.Model):

    Activity_name = models.CharField(max_length = 125)
    Department = models.CharField(max_length = 125)
    Active_employees = models.CharField(max_length = 125)
    Status = models.CharField(max_length = 125)
    
