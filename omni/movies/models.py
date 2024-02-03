from django.db import models

# Create your models here.

class movies(models.Model):
    id = models.IntegerField(unique=True, primary_key = True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=6000)
    imgPath = models.CharField(max_length=300)
    duration = models.IntegerField()
    genre = models.CharField(max_length=300)
    language = models.CharField(max_length=30)
    userRating = models.CharField(max_length=10)

    class Meta:
        db_table = "movies"


class mpaaRating(models.Model):
    id = models.OneToOneField(movies, primary_key = True, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    label = models.CharField(max_length=300)

    class Meta:
        db_table = "mpaaRating"