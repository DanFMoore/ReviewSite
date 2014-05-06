from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

 # Examples:
    # url(r'^$', 'bookies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
url_list = ['', url(r'^admin/', include(admin.site.urls))]

# for each installed app, append the list of urls
# this avoids every app having to appear in a sub-folder
from bookies.settings import INSTALLED_APPS

for app_name in INSTALLED_APPS:
	try:
		app = __import__(app_name, fromlist=['urls'])
		url_list = url_list + app.urls.urlpatterns
	except AttributeError:
		pass

urlpatterns = patterns(*url_list)
