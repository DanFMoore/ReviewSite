from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     # ex: /about-us/
    url(r'^(?P<slug>\s+)/$', views.page, name='page'),
]