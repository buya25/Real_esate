import json

from django.http import JsonResponse
from django.urls import path
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
    categories = Category.objects.all()
    agents = Agents.objects.all()
    context = {'agents': agents, 'categories': categories}
    return render(request, 'main/agent.html', context)


def blog_page(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    context = {'blogs': blogs, 'categories': categories}
    return render(request, 'main/blog.html', context)


def submit_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        user_name = request.POST.get('username')
        comment_text = request.POST.get('comment')

        # Create a new comment object and associate it with the blog
        comment = Comment(blog=blog, user_name=user_name, comment_text=comment_text)
        comment.save()

        # Return a JSON response indicating success
        return render(request, 'main/blog.html')

    # Return a JSON response indicating failure
    return JsonResponse({'success': False})


def contact_page(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'main/contact.html', context)
