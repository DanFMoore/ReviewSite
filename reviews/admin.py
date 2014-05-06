from django.contrib import admin
from reviews.models import (Operator, Game, Site, PaymentOption, Attribute,
	Pro, Con, Offer, Language)

#inlines for sites
class AttributeInline(admin.TabularInline):
    model = Attribute

class ProInline(admin.TabularInline):
	model = Pro

class ConInline(admin.TabularInline):
	model = Con

class OfferInline(admin.TabularInline):
	model = Offer

class SiteAdmin(admin.ModelAdmin):
	inlines = [AttributeInline, ProInline, ConInline, OfferInline]

	fields = ('name', 'slug', 'order',
		#page content fields
		'title', 'html_title', 'meta_desc', 'keywords',
		#emd page content fields
		'operator', 'date_added', 'date_established',
		'affiliate_link', 'visible_link', 'rating', 'games', 'deposit_options',
		'withdrawal_options', 'languages', 'review', 'content')

class DefaultAdmin(admin.ModelAdmin):
	pass

admin.site.register(Operator, DefaultAdmin)
admin.site.register(Game, DefaultAdmin)
admin.site.register(PaymentOption, DefaultAdmin)
admin.site.register(Language, DefaultAdmin)

admin.site.register(Site, SiteAdmin)