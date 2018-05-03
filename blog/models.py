from django.db import models
from django.utils import timezone
import datetime

class Blog(models.Model):
	"""docstring for Blog"""
	# def __init__(self, arg):
	# 	super(Blog, self).__init__()
	# 	self.arg = arg
	blog_title = models.CharField(max_length=100)
	blog_content = models.TextField(max_length=10000)
	blog_author = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.blog_title