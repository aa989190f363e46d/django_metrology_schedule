from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from instruments.models import InstrumentType, InstrumentType


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
    model = InstrumentType
    template_name = 'item_delete.html'
    success_url = reverse_lazy('instrument_type_list')
    extra_context = {
        'item_model_name': 'instrument type',
        }
        
    def test_func(self):
        return self.request.user.is_staff
