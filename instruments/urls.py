from django.urls import path

from common.utils import append_CRUD
from instruments.views import (
    InstrumentCatalog,
    )

urlpatterns = [
    path(
        '',
        InstrumentCatalog.as_view(),
        name='instr_catalog',
        ),
    ]

append_CRUD(
    urlpatterns,
    'instruments',
    'InstrumentType',
    'instrument_type',
    )

append_CRUD(
    urlpatterns,
    'instruments',
    'Instrument',
    'instrument',
    )
