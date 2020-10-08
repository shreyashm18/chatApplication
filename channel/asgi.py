"""
ASGI config for channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channel.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel.settings')

application = get_asgi_application()
application = get_default_application()
