from django.db import models

class Appointment(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=50)
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    appointment_datetime = models.CharField(max_length=100)

    class Meta:
        db_table = "appointments"
        managed = False