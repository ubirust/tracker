from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
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

        if 'delete' in request.POST:
            consumed_food_id = request.POST['delete']
            consumed_food = Consume.objects.get(id=consumed_food_id)
            consumed_food.delete()

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



@require_http_methods(["POST", "DELETE"])
def delete_consumed_food(request, pk):
    print('Я здесь')
    if not request.htmx:
        return HttpResponse(status=400)

    consumed_food = get_object_or_404(Consume, pk=pk)
    consumed_food.delete()

    return HttpResponse('')


tasks = [
        {'id': 1, 'name': 'Task 1'},
        {'id': 2, 'name': 'Task 2'},
        {'id': 3, 'name': 'Task 3'},
    ]
def test(request):

    return render(request, 'test.html', {'tasks': tasks})

def delete_task(request, task_id):
    # Удалить task_id из списка задач
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            break
    print(tasks)

    return render(request, 'test.html', {'tasks': tasks})