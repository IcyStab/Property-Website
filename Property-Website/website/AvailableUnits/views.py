
from .models import Listings
from django.views.generic import ListView, DetailView

# Create your views here.

class HomeView(ListView):
    model = Listings
    template_name = 'listings_list.html'
