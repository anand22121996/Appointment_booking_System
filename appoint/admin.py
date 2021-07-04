from django.contrib import admin
from . models import Time_Slot, Appointment


# # Register your models here.
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ['appointment_id','date','time_alloted']

# @admin.register(Doctor_profile)
# class Doctor_profile_Admin(admin.ModelAdmin):
#     list_display = ['id','name','email','phone','is_available']

@admin.register(Time_Slot)
class Time_Slot_Admin(admin.ModelAdmin):
    list_display = ['id','date','from_time','to_time']

@admin.register(Appointment)
class Appointment_Admin(admin.ModelAdmin):
    list_display = ['id','adate','afrom_time','ato_time','client']



