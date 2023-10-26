from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import IceCream
from .forms import IceCreamForm
from django.urls import reverse_lazy
# Create your views here.

class IceCreamListView(ListView):
    model = IceCream
    template_name = 'ice_cream_list.html'  
    context_object_name = 'ice_creams'

class IceCreamCreateView(CreateView):
    model = IceCream
    form_class = IceCreamForm
    template_name = 'ice_cream_create.html'
    success_url = reverse_lazy('ice_cream_list')