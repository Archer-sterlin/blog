from django import forms
from .models import Post


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','title', 'body', 'slug', 'image',)