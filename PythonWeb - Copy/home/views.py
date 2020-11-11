from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,Http404
from .models import Profile
from django.contrib.auth.models import User
from blog.models import Post
from account.forms import ProfileForm
# Create your views here.

class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        user_profile = User.objects.get(id=profile.user_id)
        user_post = Post.objects.filter(author=user_profile).order_by("-date")
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        
        context["profile"] = profile
        context["user_post"] = user_post
        return context

class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile2.html'
    fields=('bio','profile_pic')

    success_url = reverse_lazy('blog')

def profile_update(request, pk):
    instance = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('show_profile',args=[request.user.profile.id]))
    context = {
        'instance' : instance,
        'form' : form
    }
    return render(request, 'registration/edit_profile.html', context)    



class CreateProfileView(generic.CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    form_class = ProfileForm
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('show_profile', args=[str(self.object.pk)])
    
    

    


