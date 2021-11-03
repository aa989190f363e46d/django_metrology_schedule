from django.contrib import admin

from verifications.models import (
    VerificationScheduleEvent,
    VerificationEvent,
    )

admin.site.register(VerificationScheduleEvent)
admin.site.register(VerificationEvent)
