from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class InstrumentCatalog(TemplateView):
    template_name = 'instr_catalog.html'
