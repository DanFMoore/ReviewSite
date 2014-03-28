from django.db import models
import content

class OrderMeta:
	ordering = ['order']

class Operator(models.Model):
	"""Company that runs the websites"""
	name = models.CharField(max_length=200)

class Game(models.Model):
	"""Game available at a website (texas holdem, football etc)"""
	name = models.CharField(max_length=200)
	order = models.IntegerField()

class Language(models.Model):
	"""Language that a website is available in"""
	name = models.CharField(max_length=200)
	native_name = models.CharField(max_length=200)
	order = models.IntegerField()

	Meta = OrderMeta

class PaymentOption(models.Model):
	"""Method of withdrawing or depositing money to a website"""
	name = models.CharField(max_length=200)
	order = models.IntegerField()

	Meta = OrderMeta

class Site(models.Model):
	"""Website such as betfair, betfred etc"""
	name = models.CharField(max_length=200)
	rating = models.IntegerField()
	date_added = models.DateTimeField()
	date_established = models.DateTimeField()
	review = models.TextField()
	affiliate_link = models.CharField(max_length=200)
	visible_link = models.CharField(max_length=200)
	order = models.IntegerField()
	slug = models.SlugField()

	operator = models.ForeignKey(Operator)
	games = models.ManyToManyField(Game)
	deposit_options = models.ManyToManyField(PaymentOption, related_name = 'deposit_options')
	withdrawal_options = models.ManyToManyField(PaymentOption, related_name = 'withdrawal_options')
	content = models.OneToOneField(content.models.Content)

	def get_latest_offer(self):
		try:
			return self.offers[0]
		except IndexError:
			return None

	Meta = OrderMeta

class Attribute(models.Model):
	"""Key / value pair linked to a website"""
	key = models.CharField(max_length=200)
	value = models.CharField(max_length=200)
	order = models.IntegerField()
	site = models.ForeignKey(Site)

	Meta = OrderMeta

class Offer(models.Model):
	"""An offer such as deposit £100 and get £20 free etc"""
	info = models.TextField()
	date_added = models.DateTimeField()
	affiliate_link = models.CharField(max_length=200)
	visible_link = models.CharField(max_length=200)
	site = models.ForeignKey(Site)
	order = models.IntegerField()

	Meta = OrderMeta

class ProAndCon(models.Model):
	text = models.CharField(max_length=200)
	order = models.IntegerField()

	class Meta:
		ordering = ['order']
		abstract = True

class Pro(ProAndCon):
	"""A plus point for the website"""
	site = models.ForeignKey(Site)

class Con(ProAndCon):
	"""A bad point for the website"""
	site = models.ForeignKey(Site)