from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

# Category:
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# Note:
class Note(models.Model):
    headline = models.CharField(max_length=150)
    text = models.TextField()
    categories = models.ForeignKey(Category, on_delete=CASCADE)
