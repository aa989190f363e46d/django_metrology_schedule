from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.forms import TextInput, MultiWidget, DateTimeField
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, reverse_lazy

from instruments.models import Instrument
from referencies.models import Validator


class VerificationScheduleEvent(models.Model):
    """Модель события плана поверки."""

    instrument = models.ForeignKey(
        Instrument,
        limit_choices_to={'sweep_mark': False},
        on_delete=models.CASCADE,
        related_name='instrument',
        help_text=_('Verifiable instrument'),
        error_messages={
            'required': _('Instrument is requred'),
            },
        verbose_name=_('Instrument'),
        )

    validator = models.ForeignKey(
        Validator,
        limit_choices_to={'sweep_mark': False},
        on_delete=models.CASCADE,
        related_name='validator',
        help_text=_('Validator'),
        error_messages={
            'required': _('Validator is requred'),
            },
        verbose_name=_('Validator'),
        )

    date = models.DateField(
        help_text=_('Event date'),
        error_messages={
            'required': _('Event date is requred'),
            },
        verbose_name=_('Event date'),
        )

    sweep_mark = models.BooleanField(
        default=False,
        help_text=_('Set if item no more be applyable'),
        verbose_name=_('Hidden'),
        )

    def __str__(self):
        mark = '✓'
        try:
            self.verificationevent
        except ObjectDoesNotExist:
            mark = ''
    
        return f'{self.date} {self.instrument} {mark}'

    def get_absolute_url(self):
        return reverse(
            'verification_schedule_event_details',
            args=(self.id,),
            )

    def get_details(self, fields):
        return {field: getattr(self, field) for field in fields}


class VerificationEvent(models.Model):
    """Модель события поверки."""

    schedule_event = models.OneToOneField(
        VerificationScheduleEvent,
        on_delete=models.CASCADE,
        primary_key=True,
        help_text=_('Planned event for realization'),
        error_messages={
            'required': _('Event is requred'),
            },
        verbose_name=_('Shedule event'),
        )

    date = models.DateField(
        help_text=_('Event date'),
        error_messages={
            'required': _('Event date is requred'),
            },
        verbose_name=_('Event date'),
        )

    """
    1   ЭКСПЛУАТАЦИЯ
    2   ХРАНЕНИЕ
    3   РЕМОНТ
    4   НЕ ПОВЕРЕН
    """
    RESULT_CHOICES = (
        (1, _('Exploitation')),
        (2, _('Preservation')),
        (3, _('Repairation')),
        (4, _('Not validated')),
        )

    result = models.PositiveSmallIntegerField(
        choices=RESULT_CHOICES,
        error_messages={
            'required': _('Result is requred'),
            },
        )

    sweep_mark = models.BooleanField(
        default=False,
        help_text=_('Set if item no more be applyable'),
        verbose_name=_('Hidden'),
        )

    def __str__(self):
        instrument = self.schedule_event.instrument
        return f'{self.date} {instrument} {self.result}'

    def get_absolute_url(self):
        return reverse('verification_event_details', args=(self.id,))

    def get_details(self, fields):
        return {field: getattr(self, field) for field in fields}
