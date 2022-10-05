from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.

<<<<<<< HEAD
class ActivityList(models.Model):
    Activity_Id = models.AutoField
    Activity_name = models.CharField(max_length = 125)
    status = models.CharField(max_length = 125)
    Create_date = models.DateField


class Index (models.Model):
    Activity_id = models.AutoField
=======
class Activity_List(models.Model):

    Activity_Id = models.CharField(max_length = 125)
    Activity_name = models.CharField(max_length = 125)
    status = models.CharField(max_length = 125)
    Create_date = models.CharField(max_length = 125)


class Index (models.Model):
    Activity_id = models.CharField(max_length = 122)
>>>>>>> 84250e87c7213bfb318b193a0fa5670cf6677150
    Employee_id = models.CharField(max_length = 122)
    start_time =  models.DateTimeField 
    end_time = models.DateTimeField 
    Activity_date = models.DateTimeField
    transaction_id = models.CharField(max_length = 122)
    status = models.CharField(max_length = 122)
    idle_time = models.DateTimeField
    
