from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from room.models import Room

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_email = models.EmailField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.room} from {self.start_time} to {self.end_time} by {self.user_email}"

    def clean(self):
        if Booking.objects.filter(room=self.room, start_time__lt=self.end_time, end_time__gt=self.start_time).exists():
            raise ValidationError('Booking overlaps with an existing booking for this room.')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.calculate_price()
        self.full_clean()
        super().save(*args, **kwargs)

    def calculate_price(self):
        duration_hours = (self.end_time - self.start_time).total_seconds() / 3600
        self.price = self.room.room_type.pricing * duration_hours

    def cancel(self):
        if self.start_time > timezone.now() + timezone.timedelta(hours=48):
            self.is_cancelled = True
            self.save()
        elif self.start_time > timezone.now() + timezone.timedelta(hours=24):
            self.price *= 0.5
            self.is_cancelled = True
            self.save()
        else:
            self.is_cancelled = True
            self.save()