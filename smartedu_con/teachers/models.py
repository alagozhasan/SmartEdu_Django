from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField("Isim", max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=100)
    image = models.ImageField(upload_to="")
    facebook = models.URLField(max_length=100, blank=True)
    threads = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name
