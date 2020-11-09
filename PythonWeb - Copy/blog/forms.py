from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','author','category','image')

        widgets = {
           'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'id':'author-name', 'value':'','type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','category','image')

        widgets = {
           'title': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content','post','user')

        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'post': forms.TextInput(attrs={'class':'form-control', 'id':'post-id', 'value':'','type':'hidden'}),
            'user': forms.TextInput(attrs={'class':'form-control', 'id':'user-id', 'value':'','type':'hidden'}),
        }