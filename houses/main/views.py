import json

from django.core.mail import send_mail
from django.http import JsonResponse
from django.urls import path
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm

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
    categories = Category.objects.all()
    context = {'titles': titles, 'category': category, 'categories': categories}
    return render(request, 'main/properties.html', context)


def properties_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog).order_by('-pub_date')
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    blog.views += 1
    blog.save()
    context = {'blog': blog, 'comments': comments, 'categories': categories, 'blogs': blogs}
    return render(request, 'main/properties_details.html', context)


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
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    context = {'blogs': blogs, 'categories': categories}

    if request.method == 'POST':
        user_name = request.POST.get('username')
        comment_text = request.POST.get('comment')

        # Create a new comment object and associate it with the blog
        comment = Comment(blog=blog, user_name=user_name, comment_text=comment_text)
        comment.save()

        # Return a JSON response indicating success
        return render(request, 'main/blog.html', context)

    # Make sure you call the error page 404
    return render(request, blog)


def submit_comment_main(request, slug):
    blog = Blog.objects.get(slug=slug)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a new comment object
            comment = Comment(
                blog=blog,
                user_name=form.cleaned_data['user_name'],
                comment_text=form.cleaned_data['comment_text']
            )
            comment.save()

            # Update the comments count for the associated blog
            blog.update_comments_count()

            # Redirect to the blog details page
            return redirect('main:properties_details', slug=slug)
    else:
        form = CommentForm()

    context = {'form': form, 'categories': categories}
    return render(request, 'main/blog.html', context)


def reply_to_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    blog_slug = comment.blog.slug  # Retrieve the associated blog's slug    blogs = Blog.objects.all()

    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_id)
        user_name = request.POST.get('user_name')
        reply_text = request.POST.get('reply_text')

        reply = Reply(comment=comment, user_name=user_name, reply_text=reply_text)
        reply.save()

        return redirect('main:properties_details', slug=blog_slug)
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    context = {'comment_id': comment_id, 'blogs': blogs, 'categories': categories}
    return render(request, 'main/blog.html', context)


def contact_page(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'main/contact.html', context)


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send the email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            'default@gmail.com',  # Sender's email address
            ['yabsmullo0@gmail.com'],  # Recipient(s) email address
            fail_silently=False,
        )

        return render(request, 'success.html')  # Render a success page

    return render(request, 'contact_form.html')  # Render the contact form template
