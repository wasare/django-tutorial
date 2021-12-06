from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic import ListView, DetailView
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
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')


class ListCategoryView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class DetailCategoryView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    #context_object_name = 'category'


class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'category_form.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('category_list')


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')
