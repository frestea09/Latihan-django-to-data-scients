from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    def __str__(self):
        return '{}'.format(self.title)