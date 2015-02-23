from django.contrib import admin
from reviews.models import (Operator, Game, Site, PaymentOption, Attribute,
    Pro, Con, Offer, Language)

#inlines for sites, which will all be displayed in the Site Admin page
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
        #end page content fields
        'operator', 'date_added', 'date_established',
        'affiliate_link', 'visible_link', 'rating', 'games', 'deposit_options',
        'withdrawal_options', 'languages', 'review', 'content')

admin.site.register(Operator, admin.ModelAdmin)
admin.site.register(Game, admin.ModelAdmin)
admin.site.register(PaymentOption, admin.ModelAdmin)
admin.site.register(Language, admin.ModelAdmin)

admin.site.register(Site, SiteAdmin)