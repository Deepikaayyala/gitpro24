from django.shortcuts import render,redirect
from .models import Post

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'post':posts})
def add(request):
    if request.method =='POST':
        title=request.POST['title']
        author=request.POST['author']
        content=request.POST['content']
        Post.objects.create(title=title,author=author,content=content)
        return render(request, 'add.html', {'success': True})
    return render(request,'add.html')
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

