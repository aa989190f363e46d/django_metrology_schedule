from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from verifications.models import (
    VerificationScheduleEvent,
    VerificationEvent,
    )


class VerificationScheduleEventListView(ListView):
    queryset = VerificationScheduleEvent.objects.filter(
        verificationevent__isnull=True
        )
    template_name = 'verification_schedule.html'
    context_object_name = 'schedule'


class VerificationScheduleEventDetailsView(DetailView):
    model = VerificationScheduleEvent
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = context['object'].id
        context['item_model_name'] = _('event')
        context['item_edit_url'] = reverse_lazy(
            'verification_schedule_event_edit',
            kwargs={'pk': event_id},
            )
        context['item_delete_url'] = reverse_lazy(
            'verification_schedule_event_delete',
            kwargs={'pk': event_id},
            )
        context['imems_list_url'] = reverse_lazy(
            'verification_schedule_event_list',
            )
        context['details'] = context['object'].get_details(
            [
                'instrument',
                'validator',
                'date',
                'sweep_mark',
            ])
        return context


class VerificationScheduleEventCreateView(
    LoginRequiredMixin,
    CreateView,
        ):
    model = VerificationScheduleEvent
    template_name = 'item_create.html'
    fields = [
            'instrument',
            'validator',
            'date',
            'sweep_mark',
        ]


class VerificationScheduleEventUpdateView(
    LoginRequiredMixin,
    UpdateView,
        ):
    model = VerificationScheduleEvent
    template_name = 'item_edit.html'
    fields = [
            'instrument',
            'validator',
            'date',
            'sweep_mark',
        ]


class VerificationScheduleEventDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
        ):
    model = VerificationScheduleEvent
    template_name = 'item_delete.html'
    success_url = reverse_lazy('schedule')

    def test_func(self):
        return self.request.user.is_staff


class VerificationEventListView(ListView):
    model = VerificationEvent
    template_name = 'verifications_list.html'
    context_object_name = 'verifications_list'


class VerificationEventDetailsView(DetailView):
    model = VerificationEvent
    template_name = 'item_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = context['object'].id
        context['item_model_name'] = _('event')
        context['item_edit_url'] = reverse_lazy(
            'verification_event_edit',
            kwargs={'pk': event_id},
            )
        context['item_delete_url'] = reverse_lazy(
            'verification_event_delete',
            kwargs={'pk': event_id},
            )
        context['imems_list_url'] = reverse_lazy(
            'verification_event_list',
            )
        context['details'] = context['object'].get_details(
            [
                'schedule_event',
                'date',
                'result',
                'sweep_mark',
            ])
        return context


class VerificationEventCreateView(
    LoginRequiredMixin,
    CreateView,
        ):
    model = VerificationEvent
    template_name = 'item_create.html'
    fields = [
        'schedule_event',
        'date',
        'result',
        'sweep_mark',
        ]


class VerificationEventUpdateView(
    LoginRequiredMixin,
    UpdateView,
        ):
    model = VerificationEvent
    template_name = 'item_edit.html'
    fields = [
        'schedule_event',
        'date',
        'result',
        'sweep_mark',
        ]


class VerificationEventDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
        ):
    model = VerificationEvent
    template_name = 'item_delete.html'
    success_url = reverse_lazy('schedule')

    def test_func(self):
        return self.request.user.is_staff
