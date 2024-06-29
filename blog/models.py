from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model to represent a blog post.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
        )
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='liked_posts', blank=True)
    image = models.ImageField(upload_to='blog', blank=True, null=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model to represent a comment on a blog post.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
