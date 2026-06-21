from django.db import models

class Doctor(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    doctor_contact = models.CharField(max_length=100)

    class Meta:
        db_table = "doctors"
        managed = False

    def __str__(self):
        return self.doctor_name