from django.db import models

# Create your models here.

class TravelDiary(models.Model):
    date = models.DateTimeField('date published')
    heading = models.CharField(max_length = 100)
    body = models.CharField(max_length = 10000)

    def __str__(self):
        return self.heading

