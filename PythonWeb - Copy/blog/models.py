from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("blog")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(null = True, blank=True, upload_to="images/post/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts', null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()

    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comment_user")
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user.username)
    