import os

from oidc_controller.settings.base import *

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "default",
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["OIDC_DB_NAME"],
        "USER": os.environ["OIDC_DB_USER"],
        "PASSWORD": os.environ["OIDC_DB_PASSWORD"],
        "HOST": "oidc-db",
        "PORT": os.environ["OIDC_DB_PORT"],
    }
}

ACAPY_ADMIN_PORT = os.environ["ACAPY_ADMIN_PORT"]
ACAPY_TRANSPORT_PORT = os.environ["ACAPY_TRANSPORT_PORT"]


SITE_URL = os.environ["SITE_URL"]

JWT_TOKEN_VALIDITY = 720
JWT_TOKEN_ISSUER = SITE_URL
JWT_KEY_KID = "525786059b724b15b2d23033664342ff" # Make sure this is the kid that matches the RSA keypair generated in the OIDC admin interface


ACA_PY_URL = f"http://aca-py:{ACAPY_ADMIN_PORT}"
ACA_PY_TRANSPORT_URL = f"http://994143a56d38.ngrok.io" # Make sure this is an ngrok endpoint i.e. ngrok http http://localhost:5679
POLL_INTERVAL = 5000
POLL_MAX_TRIES = 12
