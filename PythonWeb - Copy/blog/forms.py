from django import forms
from .models import Post

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