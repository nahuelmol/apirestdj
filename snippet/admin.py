from django.contrib import admin
from .models import Friends, Pets, Languages, CountriesSpeakers

admin.site.register(Friends)
admin.site.register(Pets)
admin.site.register(Languages)
admin.site.register(CountriesSpeakers)
