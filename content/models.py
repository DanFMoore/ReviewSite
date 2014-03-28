from django.db import models

class Content(models.Model):
	"""Basic content data which can be used by other modules which include a related page"""
	title = models.CharField(max_length=200)
	html_title = models.CharField(max_length=200)
	meta_desc = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	content = models.TextField()

class Page(models.Model):
	"""Concrete implementation of a basic page managed by the admin"""
	slug = models.SlugField()
	content = models.OneToOneField(Content)

	def __str__(self):
		return self.content.title

class SystemPage(models.Model):
	"""A page which is required by the site to function, such as the home page or 404"""
	name = models.CharField(max_length=200)
	content = models.OneToOneField(Content)

	def __str__(self):
		return self.name