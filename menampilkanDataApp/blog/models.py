from django.db import models

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=255)
    context=models.TextField()
    def __str__(self):
        return '{}'.format(self.judul)
