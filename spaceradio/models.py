from django.db import models
import datetime

class Message(models.Model):
    date = models.DateTimeField(default = datetime.datetime.now())
    text = models.TextField(default = '')
    isread = models.NullBooleanField(default = False)

    def __str__(self):
        return self.text
