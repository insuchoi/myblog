from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.title