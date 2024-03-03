from django.contrib import admin

from food_consuming.models import Food, Consume, Exercise, ExerciseLog
# Register your models here.

admin.site.register(Food)
admin.site.register(Consume)
admin.site.register(Exercise)
admin.site.register(ExerciseLog)