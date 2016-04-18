from django import template
from django.apps import apps 

register = template.Library()


@register.filter(name="get_count")
def get_count(app_name, model_name):
    """params: model name as string
       fetches the count of objects of a model
    """
    return apps.get_model(app_name, model_name).objects.count()
