from django.db import models
from content.models import Content

class OrderMeta:
    """Used for the Meta class for related classes, in order to sort the collection by the order field"""
    ordering = ['order']


class Operator(models.Model):
    """Company that runs the websites"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Game(models.Model):
    """Game available at a website (texas holdem, football etc)"""
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Language(models.Model):
    """Language that a website is available in"""
    name = models.CharField(max_length=200)
    native_name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return self.name

    Meta = OrderMeta


class PaymentOption(models.Model):
    """Method of withdrawing or depositing money to a website"""
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return self.name

    Meta = OrderMeta


class Site(Content):
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
    logo = models.ImageField(null=True, blank=True, upload_to="sites/logos/")

    operator = models.ForeignKey(Operator, related_name='sites')
    games = models.ManyToManyField(Game)
    languages = models.ManyToManyField(Language)
    deposit_options = models.ManyToManyField(PaymentOption, related_name = 'deposit_options')
    withdrawal_options = models.ManyToManyField(PaymentOption, related_name = 'withdrawal_options')

    @property
    def url(self):
        """Get the url for the site (as in for the review page, not the website itself) based on urls.py"""
        return reverse('site', kwargs={'slug': self.slug})

    @property
    def get_latest_offer(self):
        try:
            return self.offers.all[0]
        except IndexError:
            return None

    def __str__(self):
        return self.name

    Meta = OrderMeta


class Attribute(models.Model):
    """Key / value pair linked to a website"""
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    order = models.IntegerField()
    site = models.ForeignKey(Site, related_name='attributes')

    Meta = OrderMeta


class Offer(models.Model):
    """An offer such as deposit £100 and get £20 free etc"""
    info = models.TextField()
    date_added = models.DateTimeField()
    affiliate_link = models.CharField(max_length=200)
    visible_link = models.CharField(max_length=200)
    site = models.ForeignKey(Site, related_name='offers')
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
    site = models.ForeignKey(Site, related_name='pros')


class Con(ProAndCon):
    """A bad point for the website"""
    site = models.ForeignKey(Site, related_name='cons')