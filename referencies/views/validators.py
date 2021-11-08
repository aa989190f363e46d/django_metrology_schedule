from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from referencies.models import Validator

class ValidatorListView(ListView):
    queryset = Validator.objects.exclude(sweep_mark=True)
    template_name = 'validators_list.html'
    context_object_name = 'validators_list'


class ValidatorDetailsView(DetailView):
    model = Validator
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        validator_id = context['object'].id
        context['item_model_name'] = _('validtor')
        context['item_edit_url'] = reverse_lazy(
            'validator_edit',
            kwargs={'pk': validator_id},
            )
        context['item_delete_url'] = reverse_lazy(
            'validator_delete',
            kwargs={'pk': validator_id},
            )
        context['imems_list_url'] = reverse_lazy('validator_list')
        context['details'] = context['object'].get_details(
            [
                'contragent',
                'license_number',
                'license_expiry_date',
                'sweep_mark',
            ])
        return context


class ValidatorCreateView(
    LoginRequiredMixin,
    CreateView,
        ):
    model = Validator
    template_name = 'item_create.html'
    fields = [
        'contragent',
        'license_number',
        'license_expiry_date',
        'sweep_mark',
        ]


class ValidatorUpdateView(
    LoginRequiredMixin,
    UpdateView,
        ):
    model = Validator
    template_name = 'item_edit.html'
    fields = [
        'contragent',
        'license_number',
        'license_expiry_date',
        'sweep_mark',
        ]


class ValidatorDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
        ):
    model = Validator
    template_name = 'item_delete.html'
    success_url = reverse_lazy('validator_list')

    def test_func(self):
        return self.request.user.is_staff
