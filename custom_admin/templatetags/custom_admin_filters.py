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
def get_model_details(registered_models):
    models_dict = {}
    for model in registered_models:
        app_label = model._meta.app_label
        info = (app_label, model._meta.model_name)
        model.add_url = reverse('admin:%s_%s_add' % info, current_app=model._meta.model_name)
        model.change_url = reverse('admin:%s_%s_changelist' % info, current_app=model.__class__.__name__)
        model.app_name =  model._meta.model_name
    return registered_models
