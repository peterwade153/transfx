import dj_database_url
from .base import *


DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=500, ssl_require=True)
