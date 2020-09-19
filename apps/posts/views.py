from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Comments
from django.utils import timezone

# Create your views here.

def Post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'posts/post_list.html',{'posteos':posts})

def Post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'posts/post_detail.html', {'posteo': post})

def Post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/posts/lista/', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'posts/post_edit.html', {'form': form})


def Post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})

#@login_required
def Add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('/posts/lista/', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/add_comment_to_post.html', {'form': form})