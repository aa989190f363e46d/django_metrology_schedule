from django.db import models
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, reverse_lazy


from referencies.models import Place


class InstrumentType(models.Model):
    """Модель измерительного прибора."""

    TITLE_LENGTH = 255
    title_err_template = _('Title must be a upto %(length)s symbols text')
    title = models.CharField(
        max_length=TITLE_LENGTH,
        unique=False,
        help_text=_('Unique if possible instrument name'),
        error_messages={
            'required': _('Title is requred'),
            'max_length': format_lazy(
                title_err_template,
                length=TITLE_LENGTH,
                ),
            },
        verbose_name=_('Title'),
        )

    INTERVALS_CHOICES = (
        (6,  _('6 mo.')),
        (12, _('12 mo.')),
        (24, _('24 mo.')),
        (36, _('36 mo.')),
        (48, _('48 mo.')),
        (60, _('60 mo.')),
        (72, _('72 mo.')),
        (96, _('96 mo.')),
        )

    default_validation_interval = models.PositiveSmallIntegerField(
        choices=INTERVALS_CHOICES,
        error_messages={
            'required': _('Validation interval is requred'),
            },
        )
    
    PR_CLS_LENGTH = 255
    pr_cls_template = _('Precision class must be a upto %(length)s symbols text')
    precision_class = models.CharField(
        max_length=PR_CLS_LENGTH,
        unique=False,
        help_text=_('Instrument precision class'),
        error_messages={
            'required': _('Prec. class is requred'),
            'max_length': format_lazy(
                pr_cls_template,
                length=PR_CLS_LENGTH,
                ),
            },
        verbose_name=_('Precision class'),
        )
    precision_lower_bound = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        help_text=_('decimal [10,5]'),
        verbose_name=_('Precision lower bound'),
        )

    precision_upper_bound = models.DecimalField(
        max_digits=10,
        decimal_places=5,
        help_text=_('decimal [10,5]'),
        verbose_name=_('Precision upper bound'),
        )

    sweep_mark = models.BooleanField(
        default=False,
        help_text=_('Set if item no more be applyable'),
        verbose_name=_('Hidden'),
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instrument_type_details', args=(self.pk,))

    def get_details(self, fields):
        return {field: getattr(self, field) for field in fields}


class Instrument(models.Model):
    """Измерительный прибор."""

    instrument_type = models.ForeignKey(
        InstrumentType,
        limit_choices_to={'sweep_mark': False},
        on_delete=models.CASCADE,
        related_name='instruments',
        help_text=_('Instrument type'),
        error_messages={
            'required': _('type is requred'),
            },
        verbose_name=_('Instrument type'),
        )

    displacement = models.ForeignKey(
        Place,
        limit_choices_to={'sweep_mark': False},
        on_delete=models.CASCADE,
        related_name='instruments',
        help_text=_('Displacement'),
        error_messages={
            'required': _('Displacement is requred'),
            },
        verbose_name=_('Instrument displacement'),
        )

    TITLE_LENGTH = 255
    title_err_template = _('Title must be a upto %(length)s symbols text')
    title = models.CharField(
        max_length=TITLE_LENGTH,
        unique=False,
        help_text=_('Unique if possible instrument name'),
        error_messages={
            'required': _('Title is requred'),
            'max_length': format_lazy(
                title_err_template,
                length=TITLE_LENGTH,
                ),
            },
        verbose_name=_('Title'),
        )

    ACC_ID_LENGTH = 10
    acc_id_err_template = _('Acc. ID must be a upto %(length)s symbols text')
    accouning_id = models.CharField(
        max_length=ACC_ID_LENGTH,
        unique=True,
        help_text=_('Unique acc. ID'),
        error_messages={
            'required': _('Acc. ID is requred'),
            'max_length': format_lazy(
                acc_id_err_template,
                length=ACC_ID_LENGTH,
                ),
            },
        verbose_name=_('Acc. ID'),
        )

    """
    Разделы отчета.

    1. Средства измерений, подлежащие государственной поверке в
    территориальном органе Госстандарта по месту нахождения объекта
    народного хозяйства
    2. Средства измерений, поверяемые юридическими лицами, не входящими
    в ГМС
    3. Средства измерений, поверяемые вне зоны обслуживания
    территориального органа Госстандарта
    """
    REPORT_PART_CHOICES = (
        (1, _('Part one')),
        (2, _('Part two')),
        (3, _('Part three')),
        )

    part_of_reports = models.PositiveSmallIntegerField(
        choices=REPORT_PART_CHOICES,
        error_messages={
            'required': _('Part of report is requred'),
            },
        )

    """
    Категории.

    1. Эталоны
    2. Средства измерений, предназначенные для применения в сфере
    законодательной метрологии
    3. Средства измерений, предназначенные для применения вне сферы
    законодательной метрологии
    """
    CATHEGORY_CHOICES = (
        (1, _('Instr. cat. one')),
        (2, _('Instr. cat. two')),
        (3, _('Instr. cat. three')),
        )

    category = models.PositiveSmallIntegerField(
        choices=CATHEGORY_CHOICES,
        error_messages={
            'required': _('Cathegory is requred'),
            },
        )

    sweep_mark = models.BooleanField(
        default=False,
        help_text=_('Set if item no more be applyable'),
        verbose_name=_('Hidden'),
        )

    def __str__(self):
        return f'{self.accouning_id} {self.title}'

    def get_absolute_url(self):
        return reverse('instrument_details', args=(self.pk,))

    def get_details(self, fields):
        return {field: getattr(self, field) for field in fields}
