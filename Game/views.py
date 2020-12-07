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
    def get(self, request):
        tasks = list(Item.objects.values())

        if request.is_ajax():
            return JsonResponse({'tasks': tasks}, status=200)

        return render(request, 'game/quizInVue.html')

#     def post(self, request):
#         bound_form = QuizForm(request.POST)

#         if bound_form.is_valid():
#             new_task = bound_form.save()
#             return JsonResponse({'task': model_to_dict(new_task)}, status=200)

#         return redirect('vue_django')


# class TaskComplete(ListView):
#     def post(self, request, id):
#         task = Choice.objects.get(id=id)
#         task.completed = True
#         task.save()
#         return JsonResponse({'task': model_to_dict(task)}, status=200)
