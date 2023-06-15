from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def home(request):
    categories = Category.objects.all()
    users = Client.objects.all()
    agents = Agents.objects.all()
    blogs = Blog.objects.all()
    comments = Comment.objects.all()

    context = {'categories': categories, 'users': users, 'agents': agents, 'blogs': blogs, 'comments': comments}

    return render(request, 'main/index.html', context)


def category_detail_view(request, slug):
    category = Category.objects.get(slug=slug)
    titles = Title.objects.filter(category=category).order_by('-date_created')
    category_values = category._meta.fields
    context = {'category': category, 'titles': titles, 'category_values': category_values}
    return render(request, 'main/properties.html', context)


def agent_page(request):
    return render(request, 'main/agent.html')


def blog_page(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'main/blog.html', context)


def contact_page(request):
    return render(request, 'main/contact.html')


def gallery_page(request):
    return render(request, 'main/gallery.html')
