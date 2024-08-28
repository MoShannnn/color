from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=255)
    hex = models.CharField(max_length=7)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="colors")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="colors")

    def __str__(self):
        return self.name

class SeasonInfo(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="info")
    description = models.TextField()

    def __str__(self):
        return self.season.name
