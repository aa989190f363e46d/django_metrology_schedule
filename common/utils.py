from django.utils.module_loading import import_string
from django.urls import path

def append_CRUD(url_patterns, app_name, model_name, path_prefix):
    for action, subpath, view in (
        ('list',    'list',             'ListView'),
        ('create',  'new',              'CreateView'),
        ('details', '<int:pk>',         'DetailsView'),
        ('edit',    '<int:pk>/edit',    'UpdateView'),
        ('delete',  '<int:pk>/delete',  'DeleteView'),
            ):

        module_name = f'{model_name}{view}'
        url_patterns.append(
            path(
                f'{path_prefix}/{subpath}',
                import_string(f'{app_name}.views.{module_name}').as_view(),
                name=f'{path_prefix}_{action}',
                ),
            )
