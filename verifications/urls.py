from django.urls import path

from common.utils import append_CRUD
from verifications.views import (
    Schedule,
    )

urlpatterns = [
    path(
        '',
        Schedule.as_view(),
        name='schedule',
        ),
]


append_CRUD(
    urlpatterns,
    'verifications',
    'verification_schedule_event',
    'validator',
    )
append_CRUD(
    urlpatterns,
    'verifications',
    'VerificationEvent',
    'verification_event',
    )
