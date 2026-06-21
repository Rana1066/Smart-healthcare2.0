from django.db import models

class Treatment(models.Model):
    procedure_id = models.IntegerField(primary_key=True)
    procedure_name = models.CharField(max_length=255)
    appointment_id = models.IntegerField()

    class Meta:
        db_table = "treatments"
        managed = False