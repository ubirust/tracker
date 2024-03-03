from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)


class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories_burned_per_10_minutes = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} - {self.date}"