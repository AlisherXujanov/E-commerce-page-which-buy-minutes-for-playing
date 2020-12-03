from Game import models
from django.shortcuts import render
from .models import Item, Order, OrderItem, Timer
from django.views.generic import ListView, DetailView, CreateView


class product(CreateView):
    model = Timer
    fields = ['name', 'difficulty']
    template_name = 'product.html'


def checkout(request):
    return render(request, "checkout.html")


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home.html', context)


class HomeListView(ListView):
    model = Item
    template_name = 'home.html'
