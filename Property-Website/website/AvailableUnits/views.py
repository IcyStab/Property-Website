from django.shortcuts import render
from django.views import generic
from .models import Listings

# Create your views here.
class PostList(generic.ListView):
    queryset = Listings.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Listings
    template_name = 'post_detail.html'