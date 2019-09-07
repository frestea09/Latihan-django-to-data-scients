from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField()
    datePost = models.DateField()
    rate = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.title)