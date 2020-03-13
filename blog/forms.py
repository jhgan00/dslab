from blog.models import *
from django import forms

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea, label='')
	class Meta:
		model = Comment
		fields = ('content',)