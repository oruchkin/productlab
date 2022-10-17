from django.db import models

# Create your models here.


class Product(models.Model):
    docfile = models.FileField(upload_to='documents/', blank=True, null=True)
    article = models.CharField(max_length = 20, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.docfile}")