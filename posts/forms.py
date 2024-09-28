from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'this is placeholder'}),
            'content': forms.Textarea(attrs={'placeholder': 'need content'})}
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('* cannot be included')
        return title
