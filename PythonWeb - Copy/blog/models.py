from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
import operator
from home.models import Profile

# Create your models here.
class CategoryManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = Q(name__icontains=query)
            qs = qs.filter(or_lookup).distinct()
        return qs

class Category(models.Model):
    name = models.CharField(max_length=200)

    objects = CategoryManager()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("blog")
    
class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (
                Q(title__icontains=query)|
                Q(body__icontains=query)|
                Q(author__username__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct()
        return qs

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(null = True, blank=True, upload_to="images/post/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255,default="Click to link to read post!!")
    likes = models.ManyToManyField(User, related_name='blog_posts', null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()

    objects = PostManager()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comment_user")
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user.username)
    