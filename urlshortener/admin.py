from django.contrib import admin
from urlshortener.models.shortner import Shortner


# Register your models here.


class ShortnerAdmin(admin.ModelAdmin):

    list_display = [
        'long_url',
        'short_url',

    ]


admin.site.register(Shortner,ShortnerAdmin)
