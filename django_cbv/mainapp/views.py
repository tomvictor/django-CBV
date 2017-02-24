from django.shortcuts import render
from mainapp.models import Profile
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.

class home_page(TemplateView):
    template_name = "home.html"


class profile_list_view(ListView):
    model = Profile
    template_name = "list.html"
    context_object_name = "object_list"


class profile_detail_view(DetailView):
    model = Profile
    context_object_name = "object"
    template_name = "detail.html"
