from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import DateTimeField


# Create your models here.


class ActivityList(models.Model):
    Activity_Id = models.AutoField
    Activity_name = models.CharField(max_length = 125)
    status = models.CharField(max_length = 125)
    Create_date = models.DateTimeField



class Activity_List(models.Model):

    Activity_Id = models.CharField(max_length = 125)
    Activity_name = models.CharField(max_length = 125)
    status = models.CharField(max_length = 125)
    Create_date = models.CharField(max_length = 125)


class Index (models.Model):
    Activity_id = models.CharField(max_length = 122)
    Employee_id = models.CharField(max_length = 122)
    start_time =  models.DateTimeField 
    end_time = models.DateTimeField 
    Activity_date = models.DateTimeField
    transaction_id = models.CharField(max_length = 122)
    status = models.CharField(max_length = 122)
    idle_time = models.DateTimeField

class logins(models.Model):
    username = models.CharField(max_length = 22)
    password = models.CharField(max_length = 22)
    
