from django.shortcuts import render, get_object_or_404
from django.http import Http404
from content.models import Page

def index(request):
    latest_page_list = Page.objects.order_by('-slug')[:5]

    context = {
        'latest_page_list': latest_page_list,
    }

    return render(request, 'content/index.html', context)

def detail(request, page_id):
    raise Http404
    return render(request, 'content/detail.html', {'page': page_id})

def fallback(request, fall_id):
    raise Http404
    return render(request, 'content/fallback.html', {'id': fall_id})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)