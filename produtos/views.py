from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from produtos.models import Category
# Create your views here.

def index(request):
    return HttpResponse('Olá Django! (index)')


def ola(request):
    return HttpResponse('Olá, Django!')


class CreateCategoryView(CreateView):
    model = Category
    fields = ('name', 'description')
    template_name = 'create_category.html'
    success_url = reverse_lazy('list_category')


class ListCategoryView(ListView):
    model = Category
    template_name = 'list_category.html'
    context_object_name = 'categories'