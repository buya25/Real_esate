from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def home(request):
    categories = Category.objects.all()

    context = {'categories': categories}

    return render(request, 'main/index.html', context)


def category_detail_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = {
        'category': category,
    }
    return render(request, 'main/properties.html', context)


def category_list_view(request):
    try:
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }
        return render(request, 'category_list.html', context)
    except Exception as e:
        # Handle the exception
        error_message = str(e)  # Convert the exception to a string
        context = {
            'error_message': error_message,
        }
        return render(request, 'error.html', context)
