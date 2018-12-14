"""
WSGI config for bonbackup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/ubuntu/backupmanager/bonbackup/bonbackup/dashboard')
sys.path.append('/home/ubuntu/backupmanager/bonbackup/bonbackup')
sys.path.append('/home/ubuntu/backupmanager/bonbackup')
sys.path.append("/usr/local/lib/python3.6/dist-packages")
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bonbackup.settings')

application = get_wsgi_application()
