from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def home(request):
    categories = Category.objects.all()

    context = {'categories': categories}

    return render(request, 'main/index.html', context)
