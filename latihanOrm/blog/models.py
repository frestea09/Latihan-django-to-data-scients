from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.TextField(max_length=50)
    rating = models.IntegerField()
    category = models.TextField()

    def __str__(self):
        return '{}. {}'.format(self.id,self.title)