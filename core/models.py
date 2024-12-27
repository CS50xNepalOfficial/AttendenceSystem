from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

# Create your models here.
class ScannedQR(models.Model):
    unique_id = models.CharField(max_length=100)    
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_scanned = models.BooleanField(default=False)

    class Meta:
        # Ensure unique_id is unique for each event_day
        constraints = [
            models.UniqueConstraint(
                fields=['unique_id', 'event'],
                name='unique_qr_per_day'
            )
        ]

    def __str__(self):
        return self.unique_id

