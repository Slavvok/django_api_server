from django.db import models
from django.utils import timezone

class Message(models.Model):
    date = models.DateTimeField(default = timezone.now)
    text = models.TextField()
    isread = models.NullBooleanField(default = False)

    def __str__(self):
        return self.text
