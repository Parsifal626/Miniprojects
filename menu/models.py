from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    named_url = models.CharField(max_length=255, blank=True)

    def str(self):
        return self.label
