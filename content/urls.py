from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     # ex: /5/
    url(r'^(?P<page_id>\d+)/$', views.detail, name='detail'),
    # ex: /5/
    url(r'^(?P<fall_id>\d+)/$', views.fallback, name='fallback'),
    # ex: /5/results/
    url(r'^(?P<page_id>\d+)/results/$', views.results, name='results'),
    # ex: /5/vote/
    url(r'^(?P<page_id>\d+)/vote/$', views.vote, name='vote'),
]