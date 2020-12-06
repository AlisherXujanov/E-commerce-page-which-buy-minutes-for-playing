from django.shortcuts import render
from .models import Choice
from django.views.generic import ListView, TemplateView
from core.models import Item, Timer
from random import shuffle
from django.http import JsonResponse


class GameView(TemplateView):
    models = Timer, Choice
    template_name = 'lv_one.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['queryset1'] = Choice.objects.all()
        context_data['queryset2'] = Timer.objects.all().order_by(
            '-started_time')
        return context_data
    # ordering = ['-name']
    # paginate_by = 3
    # ex = Timer.objects.all()
    # ex.delete()


class TaskView(ListView):
    def get(self, request):
        tasks = list(Item.objects.values())

        if request.is_ajax():
            return JsonResponse({'tasks': tasks}, status=200)

        return render(request, 'game/quizz2.html')

    # def post(self, request):
        # bound_form = anyForm(request.POST)
