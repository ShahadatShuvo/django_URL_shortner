from django.shortcuts import render # We will use it later

from django.http import HttpResponse, Http404, HttpResponseRedirect


# Model
from urlshortener.models.shortner import Shortner

# Custom form

from urlshortener.forms import ShortenerForm

def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortner.objects.get(short_url=shortened_part)

        shortener.times_followed += 1

        shortener.save()

        return HttpResponseRedirect(shortener.long_url)

    except:
        raise Http404('Sorry this link is broken :(')