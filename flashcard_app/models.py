from django.db import models

# Create your models here.
class Flashcards(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    image = models.ImageField('media/')

    def __str__(self):
        return self.word