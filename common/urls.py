from django.urls import path

from common.views import Desktop

urlpatterns = [
    path(
        '',
        Desktop.as_view(),
        name='home',
        ),
    ]
