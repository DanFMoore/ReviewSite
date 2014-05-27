from django.conf.urls import url
from reviews import views

urlpatterns = [
    url(r'^(?P<slug>\s+)/$', views.site, name='site'),
]