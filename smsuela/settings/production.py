"""
Production settings
- Set secret key from environment variable
"""

from .common import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()