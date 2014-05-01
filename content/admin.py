from django.contrib import admin
from content.models import Page, SystemPage

class PageAdmin(admin.ModelAdmin):
	fields = ('slug', 'title', 'html_title', 'meta_desc', 'keywords', 'content')

class SystemPageAdmin(admin.ModelAdmin):
	fields = ('name', 'title', 'html_title', 'meta_desc', 'keywords', 'content')
	readonly_fields= ('name',)
	

	def has_add_permission(self, request):
		return False

	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(Page, PageAdmin)
admin.site.register(SystemPage, SystemPageAdmin)