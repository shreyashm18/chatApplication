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

# application = get_asgi_application()
application = get_default_application()


# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
# django.setup()
# application = get_default_application()

# daphne -p 8001 channel.asgi:application