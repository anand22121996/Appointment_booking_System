from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Time_Slot(models.Model):
    date = models.DateField()
    from_time =  models.TimeField()
    to_time =  models.TimeField()


    class Meta:
       db_table='Time_Slot'
       ordering = ['date','from_time']
       get_latest_by='date'


class Appointment(models.Model):
    adate =models.DateField()
    afrom_time =  models.TimeField()
    ato_time =  models.TimeField()
    client = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
       db_table='Appointment'
       ordering = ['adate','afrom_time']
       get_latest_by='date'    
    