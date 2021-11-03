from django import forms
from django_select2 import forms as s2forms

from instruments.models import Instrument


class InstrumentTypeWidget(s2forms.ModelSelect2Widget):
    search_fields = (
        'title__icontains',
    )


class InstrumentForm(forms.ModelForm, s2forms.ModelSelect2Mixin):
    class Meta:
        model = Instrument
        fields = (
            'instrument_type',
            'displacement',
            'title',
            'accouning_id',
            'part_of_reports',
            'category',
            'sweep_mark',
        )

        # in the code below we initialize widget with select2 specific html attributes:
        # https://select2.org/configuration/data-attributes
        # if you don't need any, you can specify just a widget class
        # "instrument type": InstrumentTypeWidget,
        # you can add any other html attributes too, if needed
        widgets = {
            'instrument_type': InstrumentTypeWidget(
                attrs={
                    'data-placeholder': '-- select type --',
                    'data-ajax--delay': 250,
                    }),
        }
