from django.shortcuts import render,get_object_or_404
from django.views import generic
from . import views
from .models import Post, Category
from . import forms
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class PostCreateView(generic.CreateView):
    model = Post
    form_class = forms.PostForm
    template_name = 'blog/post_create.html'
    #fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'body','category']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class CategoryCreateView(generic.CreateView):
    model = Category
    fields=['name']
    template_name = 'blog/category_create.html'
    success_url =  reverse_lazy('post_create')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CategoryCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
 
def CategoryView(request, cats):
    cats = cats.replace('-',' ')
    category = Category.objects.get(name=cats)
    category_post = Post.objects.filter(category=category.id)
    context = {
        'category' : category,
        'category_post' : category_post,
    }
    return render(request, 'blog/category.html', context)

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    context= {
        'cat_menu_list': cat_menu_list,
    }
    return render(request, 'blog/category_list.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))
    