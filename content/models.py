from django.db import models

class Content(models.Model):
	"""Basic page data which can be used by other modules"""
	title = models.CharField(max_length=200)
	html_title = models.CharField(max_length=200)
	meta_desc = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.title

	class Meta:
		abstract = True

class Page(Content):
	"""Concrete implementation of a basic page managed by the admin"""
	slug = models.SlugField()

class SystemPage(Content):
	"""A page which is required by the site to function, such as the home page or 404"""
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name