from django.shortcuts import render, get_object_or_404
from content.models import Page, SystemPage

def index(request):
    """Display the home page"""
    page = get_object_or_404(SystemPage, name='Home Page')
    return render(request, 'content/index.html', {'page': page})

def page(request, slug):
    """Display a normal page"""
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'content/page.html', {'page': page})