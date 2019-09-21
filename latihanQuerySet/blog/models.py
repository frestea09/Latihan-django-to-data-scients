from django.db import models

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=25)
    post = models.TextField()
    kategori = models.TextField()
    rating = models.IntegerField()
    def __str__(self):
        return '{}. {}'.format(self.judul,self.post)