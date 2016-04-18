from django import template
from django.contrib.admin import site
from django.apps import apps
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter(name="get_count")
def get_count(app_name, model_name):
    """params: model name as string
       fetches the count of objects of a model
    """
    return apps.get_model(app_name, model_name).objects.count()


@register.simple_tag
def get_registered_models():
    return site._registry

@register.simple_tag
def get_django_apps(registered_models):
    models_dict = {}
    for model in registered_models:
        app_label = model._meta.app_label
        info = (app_label, model._meta.model_name)
        models_dict[app_label] = {}
        models_dict[app_label]['name'] = app_label
        models_dict[app_label]['change_url'] = reverse('admin:%s_%s_changelist' % info, current_app=model.__class__.__name__)
    return models_dict


@register.filter(name="get_item")
def get_item(model_dict, app_label, key):
    return model_dict.get(app_label).get(key)
