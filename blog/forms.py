from django import forms

class NewBlogForm(forms.Form):
	title = forms.CharField(label = 'title', max_length = 100)
	content = forms.CharField(label = 'content', max_length = 100)
	author = forms.CharField(label = 'author', max_length = 100)


