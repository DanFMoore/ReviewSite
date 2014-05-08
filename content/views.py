from django.shortcuts import render, get_object_or_404
from content.models import Page

def index(request):
    latest_page_list = Page.objects.order_by('-slug')[:5]

    context = {
        'latest_page_list': latest_page_list,
    }

    return render(request, 'content/index.html', context)

def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'content/detail.html', {'page': page})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)