from lib2to3.fixes.fix_input import context
from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from primary_app import models

# Create your views here.

# class Based View
class IndexView(View):
    def get(self, request):
        return HttpResponse('Hello, this is class view')

class TemView(TemplateView):
    template_name = 'class_app/index2.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sample_text_1'] = "sample_text_1"
        context['sample_text_2'] = "sample_text_2"
        context['sample_text_3'] = "sample_text_3"
        
        return context

class List_View(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'class_app/index2.html'
    
    
class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'class_app/musician_details.html'
    
    
class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'class_app/musician_form.html'
    
class UpdateMusician(UpdateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'class_app/musician_form.html'
    
class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('class_app:musicianlist')
    template_name = 'class_app/delete_musician.html'