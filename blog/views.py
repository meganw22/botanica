from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    """
    View to list all blog posts ordered by published date.
    """
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """
    View to display the details of a single blog post and its comments.
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user
                new_comment.save()
                messages.success(request, 'Your comment has been added!')
                return redirect('post_detail', pk=pk)
        else:
            messages.error(request, 'You need to be logged in to comment.')
            return redirect('post_detail', pk=pk)
    
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def post_new(request):
    """
    View to create a new blog post. Requires the user to be logged in.
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_detail', pk=new_post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    """
    View to edit an existing blog post. Requires the user to be the author of the post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, 'You are not authorized to edit this post.')
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def post_delete(request, pk):
    """
    View to delete a blog post. Requires the user to be an admin.
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('post_list')

@login_required
def delete_comment(request, pk):
    """
    View to delete a comment. Only the comment author can delete their comment.
    """
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        messages.error(request, 'You are not authorized to delete this comment.')
        return redirect('post_detail', pk=comment.post.pk)
    
    post_pk = comment.post.pk
    comment.delete()
    messages.success(request, 'Comment deleted successfully.')
    return redirect('post_detail', pk=post_pk)

@login_required
def like_post(request, pk):
    """
    View to handle liking a post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return redirect('post_detail', pk=pk)
