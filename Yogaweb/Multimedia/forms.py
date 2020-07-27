from django import forms
from .models import *
from django.contrib.auth.models import User


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video_list
        fields = ["Title", "Author", "VideoFile"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image_list
        fields = ('name', 'pdf')


class Blog_post_form(forms.ModelForm):
    class Meta:
        model = Post_Blog
        fields = ('title', 'author_name', 'body', 'File_f')


