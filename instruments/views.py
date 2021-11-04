from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from common.forms import InstrumentForm
from instruments.models import InstrumentType, Instrument


class InstrumentCatalog(TemplateView):
    template_name = 'instr_catalog.html'


class InstrumentTypeListView(ListView):
    queryset = InstrumentType.objects.exclude(sweep_mark=True)
    template_name = 'instrument_types_list.html'
    context_object_name = 'instrument_types_list'


class InstrumentTypeDetailsView(DetailView):
    model = InstrumentType
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instrument_type_id = context['object'].id
        context['item_model_name'] = _('instrument type')
        context['item_edit_url'] = reverse_lazy(
            'instrument_type_edit',
            kwargs={'pk': instrument_type_id},
            )
        context['item_delete_url'] = reverse_lazy(
            'instrument_type_delete',
            kwargs={'pk': instrument_type_id},
            )
        context['imems_list_url'] = reverse_lazy('instrument_type_list')
        context['details'] = context['object'].get_details(
            [
                'title',
                'precision_class',
                'precision_lower_bound',
                'precision_upper_bound',
                'default_validation_interval',
                'sweep_mark',
            ])
        return context


class InstrumentTypeCreateView(
    LoginRequiredMixin,
    CreateView,
        ):
    model = InstrumentType
    template_name = 'item_create.html'
    fields = [
        'title',
        'precision_class',
        'precision_lower_bound',
        'precision_upper_bound',
        'default_validation_interval',
        'sweep_mark',
        ]
    extra_context = {
        'item_model_name': 'instrument type',
        }


class InstrumentTypeUpdateView(
    LoginRequiredMixin,
    UpdateView,
        ):
    model = InstrumentType
    template_name = 'item_edit.html'
    fields = [
        'title',
        'precision_class',
        'precision_lower_bound',
        'precision_upper_bound',
        'default_validation_interval',
        'sweep_mark',
        ]
    extra_context = {
        'item_model_name': 'instrument type',
        }

class InstrumentTypeDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
        ):
    model = Instrument
    template_name = 'item_delete.html'
    success_url = reverse_lazy('instrument_type_list')
    extra_context = {
        'item_model_name': 'instrument type',
        }
        
    def test_func(self):
        return self.request.user.is_staff


class InstrumentListView(ListView):
    queryset = Instrument.objects.exclude(sweep_mark=True)
    template_name = 'instruments_list.html'
    context_object_name = 'instruments_list'


class InstrumentDetailsView(DetailView):
    model = Instrument
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instrument_id = context['object'].id
        context['item_model_name'] = _('instrument')
        context['item_edit_url'] = reverse_lazy(
            'instrument_edit',
            kwargs={'pk': instrument_id},
            )
        context['item_delete_url'] = reverse_lazy(
            'instrument_delete',
            kwargs={'pk': instrument_id},
            )
        context['imems_list_url'] = reverse_lazy('instrument_list')
        context['details'] = context['object'].get_details(
            [
                'instrument_type',
                'displacement',
                'title',
                'accouning_id',
                'part_of_reports',
                'category',
                'sweep_mark',
            ])
        return context


class InstrumentCreateView(
    LoginRequiredMixin,
    CreateView,
        ):
    model = Instrument
    template_name = 'item_create.html'
    form_class = InstrumentForm

    # fields = [
    #     'instrument_type',
    #     'displacement',
    #     'title',
    #     'accouning_id',
    #     'part_of_reports',
    #     'category',
    #     'sweep_mark',
    #     ]


class InstrumentUpdateView(
    LoginRequiredMixin,
    UpdateView,
        ):
    model = Instrument
    template_name = 'item_edit.html'
    form_class = InstrumentForm

    # fields = [
    #     'instrument_type',
    #     'displacement',
    #     'title',
    #     'accouning_id',
    #     'part_of_reports',
    #     'category',
    #     'sweep_mark',
    #     ]


class InstrumentDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
        ):
    model = InstrumentType
    template_name = 'item_delete.html'
    success_url = reverse_lazy('instrument_list')

    def test_func(self):
        return self.request.user.is_staff
