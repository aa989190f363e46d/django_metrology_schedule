from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from referencies.models import Place


class PlaceListView(ListView):
    queryset = Place.objects.exclude(sweep_mark=True)
    template_name = 'places_list.html'
    context_object_name = 'places_list'


class PlaceDetailsView(DetailView):
    model = Place
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        place_id = context['object'].id
        context['item_model_name'] = _('place')
        context['item_edit_url'] = reverse_lazy(
            'place_edit',
            kwargs={'pk': place_id},
            )
        context['item_delete_url'] = reverse_lazy(
            'place_delete',
            kwargs={'pk': place_id},
            )
        context['imems_list_url'] = reverse_lazy('place_list')
        context['details'] = context['object'].get_details(
            [
                'contragent',
                'title',
                'sweep_mark',
            ])
        return context


class PlaceCreateView(
    LoginRequiredMixin,
    CreateView,
        ):
    model = Place
    template_name = 'item_create.html'
    fields = [
        'contragent',
        'title',
        'sweep_mark',
        ]


class PlaceUpdateView(
    LoginRequiredMixin,
    UpdateView,
        ):
    model = Place
    template_name = 'item_edit.html'
    fields = [
        'contragent',
        'title',
        'sweep_mark',
        ]


class PlaceDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
        ):
    model = Place
    template_name = 'item_delete.html'
    success_url = reverse_lazy('validator_list')

    def test_func(self):
        return self.request.user.is_staff
