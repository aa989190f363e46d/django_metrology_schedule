from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from referencies.models import Contragent


class ContragentListView(ListView):
    queryset = Contragent.objects.exclude(sweep_mark=True)
    template_name = 'contragents_list.html'
    context_object_name = 'contragents_list'


class ContragentDetailsView(DetailView):
    model = Contragent
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contragent_id = context['object'].id
        context['item_model_name'] = _('contragent')
        context['item_edit_url'] = reverse_lazy(
            'contragent_edit',
            kwargs={'pk': contragent_id},
            )
        context['item_delete_url'] = reverse_lazy(
            'contragent_delete',
            kwargs={'pk': contragent_id},
            )
        context['imems_list_url'] = reverse_lazy('contragent_list')
        context['details'] = context['object'].get_details(
            [
                'title',
                'unp',
                'ownership_form',
                'contacts',
                'sweep_mark',
            ])
        return context


class ContragentCreateView(
    LoginRequiredMixin,
    CreateView,
        ):
    model = Contragent
    template_name = 'item_create.html'
    fields = [
        'title',
        'unp',
        'ownership_form',
        'contacts',
        'sweep_mark',
        ]


class ContragentUpdateView(
    LoginRequiredMixin,
    UpdateView,
        ):
    model = Contragent
    template_name = 'item_edit.html'
    fields = [
        'title',
        'unp',
        'ownership_form',
        'contacts',
        'sweep_mark',
        ]


class ContragentDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
        ):
    model = Contragent
    template_name = 'item_delete.html'
    success_url = reverse_lazy('contragent_list')

    def test_func(self):
        return self.request.user.is_staff
