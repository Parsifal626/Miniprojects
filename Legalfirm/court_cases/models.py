from django.db import models
from django.utils import timezone
from django.urls import reverse

class Case(models.Model):
    case_number = models.CharField(max_length=50)
    case_title = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    date_filed = models.DateTimeField(default=timezone.now)
    court = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('case_detail', kwargs={'pk': self.pk})
        

    def __str__(self):
        return self.case_title
