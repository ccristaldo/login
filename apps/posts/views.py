from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from .models import Post
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


	# form = PostForm()
	# return render(request, 'posts/post_edit.html', {'form': form})