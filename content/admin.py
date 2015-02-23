from django.contrib import admin
from content.models import Page, SystemPage, Menu, MenuLink

class PageAdmin(admin.ModelAdmin):
    fields = ('slug', 'title', 'html_title', 'meta_desc', 'keywords', 'content')

class SystemPageAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'html_title', 'meta_desc', 'keywords', 'content')
    readonly_fields= ('name',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class MenuLinkInline(admin.TabularInline):
    """Menu link admin will be contained inline within the MenuAdmin"""
    model = MenuLink

class MenuAdmin(admin.ModelAdmin):
    """Menu admin page will allow user to administer all links for that menu on the one page"""
    inlines = [MenuLinkInline]

admin.site.register(Page, PageAdmin)
admin.site.register(SystemPage, SystemPageAdmin)
admin.site.register(Menu, MenuAdmin)