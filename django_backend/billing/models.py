from django.db import models

class Billing(models.Model):
    invoice_id = models.CharField(max_length=50, primary_key=True)
    patient_id = models.IntegerField()
    items = models.CharField(max_length=255)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    class Meta:
        db_table = "billing"
        managed = False