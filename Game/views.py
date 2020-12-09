from django.shortcuts import render, redirect
from .models import Choice
from django.views.generic import ListView, TemplateView
from core.models import Item, Timer
from random import choice, shuffle
from django.http import JsonResponse
from .forms import QuizForm
from django.forms.models import model_to_dict


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


class quizInVue(ListView):
    model = Choice
    template_name = 'game/quizInVue.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['queryset1'] = Choice.objects.all()
        context_data['queryset2'] = Timer.objects.all().order_by(
            '-started_time')
        return context_data

    # def quiz(self, request):
