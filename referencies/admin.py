from django.contrib import admin

from referencies.models import Contragent, Validator, Place


class ValidatorInline(admin.TabularInline):
    model = Validator

class PlaceInline(admin.TabularInline):
    model = Place

class ContragentAdmin(admin.ModelAdmin):
    inlines = [ValidatorInline, PlaceInline]


admin.site.register(Contragent, ContragentAdmin)
admin.site.register(Validator)
admin.site.register(Place)
