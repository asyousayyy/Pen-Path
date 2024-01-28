from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    #get all the posts
    posts = Post.objects.all()
    return render(request,"blog/index.html", {"posts":posts})

def post_detail(request,post_id):
    #get single blog post if it exists
    post = get_object_or_404(Post, pk = post_id)
    return render(request,"blog/post_detail.html", {"post":post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "blog/create.html", {"form":form})
    

