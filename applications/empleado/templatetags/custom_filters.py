import os
from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='file_exists')
def file_exists(file_path):
    print(file_path)
    if not file_path:
        return False
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    return os.path.isfile(full_path)