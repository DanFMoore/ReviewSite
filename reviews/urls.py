from django.conf.urls import url
from reviews import views

urlpatterns = [
    # ex: /betfair/
    url(r'^(?P<slug>\s+)/$', views.site, name='site'),
]