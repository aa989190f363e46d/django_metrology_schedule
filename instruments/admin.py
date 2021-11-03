from django.contrib import admin

from instruments.models import Instrument, InstrumentType


class InstrumentInline(admin.TabularInline):
    model = Instrument


class InstrumentTypeAdmin(admin.ModelAdmin):
    inlines = [InstrumentInline]


admin.site.register(InstrumentType, InstrumentTypeAdmin)
admin.site.register(Instrument)
