from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Words(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.word