from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from listings.models import Listing
from realtors.models import Realtor
from listings import choices

def index(request):
    listings = Listing.objects.all()[:3]

    context = {
        "listings": listings,
        'bedroom_choices': choices.bedroom_choices,
        'state_choices': choices.state_choices,
        'price_choices': choices.price_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.all()

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    }
    return render(request, 'pages/about.html', context)