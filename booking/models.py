from django.db import models


# Create your models here.
class Slot(models.Model):
    slot_id = models.CharField(primary_key=True, max_length=15)
    slot_title = models.CharField(max_length=40)
    slot_lag = models.FloatField()
    slot_long = models.FloatField()
    slot_charges = models.IntegerField()

    def __str__(self):
        return self.slot_id + str(self.slot_charges)


class Booking(models.Model):
    slot_no = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_id = models.CharField(unique=True, null=True,max_length=15)
    cost = models.IntegerField()
    duration = models.IntegerField()
    start_timing = models.DateTimeField()
    end_timing = models.DateTimeField(blank=True,null=True)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.slot_no.slot_id + str(self.duration) + "hours"
