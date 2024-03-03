from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from food_consuming.models import Food, Consume, Exercise, ExerciseLog




# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        context['consumed_food'] = Consume.objects.filter(user=self.request.user)
        context['exercises'] = Exercise.objects.all()
        context['exercise_logs'] = ExerciseLog.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        if 'food_consumed' in request.POST:
            food_consumed = request.POST['food_consumed']
            consume = Food.objects.get(name=food_consumed)
            user = request.user
            consume = Consume(user=user, food_consumed=consume)
            consume.save()

        if 'exercise_completed' in request.POST:
            exercise_completed = request.POST['exercise_completed']
            exercise = Exercise.objects.get(name=exercise_completed)
            user = request.user
            exercise_log = ExerciseLog(user=user, exercise=exercise)
            exercise_log.save()

        return redirect('/')


class DeleteView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consumed_food'] = Consume.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        consumed_food = Consume.objects.get(id=kwargs['id'])
        consumed_food.delete()
        return redirect('/')


