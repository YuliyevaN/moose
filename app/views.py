from django.shortcuts import render
from .models import Blog, Contact, Comment


def home_view(request):
    posts = Blog.objects.filter(is_published = True)
    d = {
        'posts':posts
    }
    return render(request, 'index-2.html', context=d)

def about_view(request):
    return render(request, 'about.html')

def blog_view(request):
    posts = Blog.objects.filter(is_published = True)
    d = {
        'posts':posts
    }
    return render(request, 'blog.html', context=d)

def blog_single_view(request, pk):
    post = Blog.objects.get(id=pk)
    if request.method =='POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        website = data.get('website')
        message = data.get('message')
        obj = Comment.objects.create(name=name, email=email, website=website, message=message, post=post)
        obj.save()
    comments = Comment.objects.filter(post=post.id)
    d = {
        'post':post,
        'comments':comments
    }
    return render(request, 'blog-single.html', context=d)

def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        obj = Contact.objects.create(name=name, email=email, subject= subject, message=message)
        obj.save()

    return render(request, 'contact.html')