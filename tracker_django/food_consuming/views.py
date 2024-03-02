from django.shortcuts import render
from django.views.generic import TemplateView

from tracker_django.food_consuming.models import Food, Consume


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food'] = Food.objects.all()
        context['consumed_foods'] = Consume.objects.filter(user=self.request.user)
        return context


