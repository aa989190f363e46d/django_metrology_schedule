
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, reverse_lazy


class Contragent(models.Model):
    """Модель юридического лица."""

    TITLE_LENGTH = 255
    title_err_template = _('Title must be a upto %(length)s symbols text')
    title = models.CharField(
        max_length=TITLE_LENGTH,
        unique=False,
        help_text=_('Unique if possible contragent name'),
        error_messages={
            'required': _('Title is requred'),
            'max_length': format_lazy(
                title_err_template,
                length=TITLE_LENGTH,
                ),
            },
        verbose_name=_('Title'),
        )

    UNP_LENGTH = 9
    unp_err_template = _('UNP must be exact %(length)s symbols length')
    unp_len_err = format_lazy(unp_err_template, length=UNP_LENGTH)
    unp = models.CharField(
        max_length=UNP_LENGTH,
        db_index=True,
        unique=True,
        help_text=_('Unique tax payer number (belorussian)'),
        error_messages={
            'required': _('Title is requred'),
            'min_length': unp_len_err,
            'max_length': unp_len_err,
            },
        verbose_name=_('UNP'),
        )

    class OwnershipForms(models.TextChoices):
        '''Contain possible ownership forms.'''

        JSC = 'JSC', _('JSC')
        LTD = 'LTD', _('LTD')
        RUE = 'RUE', _('RUE')
        RDTUE = 'RDTUE', _('RDTUE')
        GU = 'GU', _('GU')

    ownership_form = models.CharField(
        max_length=15,
        choices=OwnershipForms.choices,
        error_messages={
            'required': _('Ownership form is requred'),
            },
        )

    contacts = models.TextField(
        blank=True,
        help_text=_('Contacts information'),
        #error_messages=_(''),
        verbose_name=_('Contacts'),
        )

    sweep_mark = models.BooleanField(
        default=False,
        help_text=_('Set if item no more be applyable'),
        #error_messages=_(''),
        verbose_name=_('Hidden'),
        )
    # cheef_person

    def __str__(self):
        return f'{self.unp} {self.ownership_form} {self.title}'

    def get_absolute_url(self):
        return reverse('contragent_details', args=(self.pk,))

    def get_details(self, fields):
        return {field: getattr(self, field) for field in fields}


class Validator(models.Model):
    """Модель юридического лица пверителя"""

    contragent = models.ForeignKey(
        Contragent,
        limit_choices_to={'sweep_mark': False},
        on_delete=models.CASCADE,
        related_name='valdators',
        help_text=_('Related contragent'),
        error_messages={
            'required': _('Contragent is requred'),
            },
        verbose_name=_('Contragent'),
        )

    license_number = models.CharField(
        max_length=50,
        help_text=_('Actual license number'),
        error_messages={
            'required': _('License is requred'),
            },
        verbose_name=_('License number'),
        )

    license_expiry_date = models.DateField(
        help_text=_('License expiry date'),
        error_messages={
            'required': _('License expiry date is requred'),
            },
        verbose_name=_('License expiry date'),
        )

    sweep_mark = models.BooleanField(
        default=False,
        help_text=_('Set if item no more be applyable'),
        verbose_name=_('Hidden'),
        )

    def __str__(self):
        return f'{self.license_number} {self.license_expiry_date}'

    def get_absolute_url(self):
        return reverse_lazy('validator_details', args=(self.pk,))

    def get_details(self, fields):
        return {field: getattr(self, field) for field in fields}


class Place(models.Model):
    """Модель юридического лица пверителя"""

    contragent = models.ForeignKey(
        Contragent,
        limit_choices_to={'sweep_mark': False},
        on_delete=models.CASCADE,
        related_name='places',
        help_text=_('Related contragent'),
        error_messages={
            'required': _('Contragent is requred'),
            },
        verbose_name=_('Contragent'),
        )

    TITLE_LENGTH = 255
    title_err_template = _('Title must be a upto %(length)s symbols text')
    title = models.CharField(
        max_length=TITLE_LENGTH,
        unique=False,
        help_text=_('Unique if possible place name'),
        error_messages={
            'required': _('Title is requred'),
            'max_length': format_lazy(
                title_err_template,
                length=TITLE_LENGTH,
                ),
            },
        verbose_name=_('Title'),
        )

    sweep_mark = models.BooleanField(
        default=False,
        help_text=_('Set if item no more be applyable'),
        verbose_name=_('Hidden'),
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('place_details', args=(self.pk,))

    def get_details(self, fields):
        return {field: getattr(self, field) for field in fields}
