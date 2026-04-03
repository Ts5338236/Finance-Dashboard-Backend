"""
WSGI config for finance_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_backend.settings')

application = get_wsgi_application()

if not settings.DEBUG:
    try:
        # Run migrations automatically
        call_command('migrate', interactive=False)
        
        # Import your seed logic
        from seed_data import seed
        seed()
        print("Vercel Auto-migrate and Seed complete.")
    except Exception as e:
        print(f"Vercel Startup Error: {e}")
