from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import Http404
from multiurl import multiurl, ContinueResolving

admin.autodiscover()

 # Examples:
    # url(r'^$', 'bookies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
url_list = []

# for each installed app, append the list of urls
# this avoids every app having to appear in a sub-folder
from bookies.settings import INSTALLED_APPS

for app_name in INSTALLED_APPS:
    try:
        app = __import__(app_name, fromlist=['urls'])
        url_list = url_list + app.urls.urlpatterns
    except AttributeError:
        pass

# use multiurl so that if any view raises a 404, any other view that
# matches the same url pattern can be called until a 404 is not raised
# this allows multiple views to use the same url pattern
url_list = multiurl(*url_list, catch = (Http404, ContinueResolving))
urlpatterns = patterns('', url(r'^admin/', include(admin.site.urls)), url_list)

handler404 = 'django.views.defaults.page_not_found'