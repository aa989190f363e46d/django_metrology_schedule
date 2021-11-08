from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class RefsCatalog(TemplateView):
    template_name = 'refs_catalog.html'
