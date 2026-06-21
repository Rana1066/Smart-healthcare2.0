from django.db import models

class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    full_name = models.CharField(max_length=200)
    email_domain = models.CharField(max_length=100)

    class Meta:
        db_table = "patients"
        managed = False

    def __str__(self):
        return self.full_name