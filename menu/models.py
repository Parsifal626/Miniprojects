from django.db import models

class Judgment(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    court = models.CharField(max_length=200)
    text = models.TextField()
