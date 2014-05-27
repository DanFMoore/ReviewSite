from django.shortcuts import render
from reviews.models import Site

def site(request, slug):
    """Display details for a site"""
    site = get_object_or_404(Site, slug='slug')

    return render(request, 'reviews/site.html', {
        'site': site,
        'operator': site.operator,
        'games': site.games.all(),
        'languages': site.languages.all(),
        'deposit_options': site.deposit_options.all(),
        'withdrawal_options': site.withdrawal_options.all(),
        'attributes': site.attributes.all(),
        'offers': site.offers.all(),
        'latest_offer': site.latest_offer,
        'pros': site.pros.all(),
        'cons': site.cons.all(),
    })