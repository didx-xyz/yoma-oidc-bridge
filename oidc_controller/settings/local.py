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

ACA_PY_ADMIN_PORT = os.environ["ACAPY_ADMIN_PORT"]
ACA_PY_TRANSPORT_PORT = os.environ["ACAPY_TRANSPORT_PORT"]


SITE_URL = os.environ["SITE_URL"]

JWT_TOKEN_VALIDITY = 720
JWT_TOKEN_ISSUER = SITE_URL
# Make sure this is the kid that matches the RSA keypair generated in the OIDC admin interface
JWT_KEY_KID = "525786059b724b15b2d23033664342ff"


# Running on localhost config
# ACA_PY_URL = f"http://aca-py:{ACA_PY_ADMIN_PORT}"
# ACA_PY_TRANSPORT_URL = f"http://aca-py:{ACA_PY_TRANSPORT_PORT}"

# Running with ngrok config
ACA_PY_URL = f"http://aca-py:{ACA_PY_ADMIN_PORT}"
NGROK_AGENT_URL = os.getenv("NGROK_AGENT_URL")
ACA_PY_TRANSPORT_URL = NGROK_AGENT_URL

POLL_INTERVAL = 5000
POLL_MAX_TRIES = 12


# Settings for django-oidc-rp
OIDC_RP_PROVIDER_ENDPOINT = os.getenv("OIDC_RP_PROVIDER_ENDPOINT")
OIDC_RP_PROVIDER_AUTHORIZATION_ENDPOINT = f"{OIDC_RP_PROVIDER_ENDPOINT}/vc/connect/authorize"
OIDC_RP_PROVIDER_TOKEN_ENDPOINT = f"{OIDC_RP_PROVIDER_ENDPOINT}/vc/connect/token"
OIDC_RP_PROVIDER_JWKS_ENDPOINT = f"{OIDC_RP_PROVIDER_ENDPOINT}/.well-known/openid-configuration/jwks"
OIDC_RP_PROVIDER_USERINFO_ENDPOINT = f"{OIDC_RP_PROVIDER_ENDPOINT}/vc/connect/userinfo"
OIDC_RP_CLIENT_ID = os.getenv("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_RP_CLIENT_SECRET")
OIDC_RP_PROVIDER_SIGNATURE_ALG = "RS256"
OIDC_RP_SCOPES = os.getenv("OIDC_RP_SCOPES", "openid profile vc_authn")
OIDC_RP_ID_TOKEN_INCLUDE_USERINFO = True

VC_AUTHN_PRES_REQ_CONF_ID = os.getenv("VC_AUTHN_PRES_REQ_CONF_ID")
