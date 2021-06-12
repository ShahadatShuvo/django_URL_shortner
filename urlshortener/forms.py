'''
Shortener Forms urlshortener/forms.py
'''

from django import forms

from urlshortener.models import Shortner


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = Shortner

        fields = ('long_url',)
