from django.shortcuts import render
from .models import Choice
from django.views.generic import ListView, TemplateView
from core.models import Timer
from itertools import chain, filterfalse
from django.core.paginator import Paginator

# def game(request):
#     results = Choice.objects.all()
#     return render(request, 'lv_one.html', {'Choice': results})


class GameView(TemplateView):
    models = Timer, Choice
    template_name = 'lv_one.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['queryset1'] = Choice.objects.all()
        context_data['queryset2'] = Timer.objects.all().order_by(
            '-started_time')
        return context_data
    # user_list = Timer.objects.all()
    # paginator = Paginator(user_list, 2)
    # ordering = ['-name']
    # paginate_by = 3
    ex = Timer.objects.all()
    ex.delete()
