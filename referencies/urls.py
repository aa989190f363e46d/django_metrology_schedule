from django.urls import path

from common.utils import append_CRUD
from referencies.views import (
    RefsCatalog,
    )

urlpatterns = [
    path(
        '',
        RefsCatalog.as_view(),
        name='refs_catalog',
        ),
]


append_CRUD(
    urlpatterns,
    'referencies',
    'Validator',
    'validator',
    )
append_CRUD(
    urlpatterns,
    'referencies',
    'Contragent',
    'contragent',
    )
append_CRUD(
    urlpatterns,
    'referencies',
    'Place',
    'place',
    )