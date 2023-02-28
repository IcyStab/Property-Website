
from .models import Listings
from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.

class HomeView(ListView):
    model = Listings
    template_name = 'listings_list.html'
