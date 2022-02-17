from pyexpat import model
from wsgiref.handlers import format_date_time
# from xml.etree.ElementTree import Comment
from django import forms
from .models import PostModel,Comment
# from pagedown.widgets import PagedownWidget

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    publised_on = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    class Meta:
        model = PostModel
        fields = ('title','content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Comments Here.......'}))

    class Meta:
        model = Comment
        fields = ('content',)
        
class ReplyToComments(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Reply Here.......'}))

    class Meta:
        model = Comment
        fields = ('content',)