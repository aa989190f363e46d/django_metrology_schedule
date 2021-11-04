from django.urls import path

from common.utils import append_CRUD
from verifications.views import (
    VerificationScheduleEventListView,
    )

urlpatterns = [
    path(
        '',
        VerificationScheduleEventListView.as_view(),
        name='schedule',
        ),
]

append_CRUD(
    urlpatterns,
    'verifications',
    'VerificationScheduleEvent',
    'verification_schedule_event',
    )

append_CRUD(
    urlpatterns,
    'verifications',
    'VerificationEvent',
    'verification_event',
    )
