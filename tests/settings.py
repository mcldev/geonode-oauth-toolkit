ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "example.sqlite",
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = "UTC"

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ""
MEDIA_URL = ""

STATIC_ROOT = ""
STATIC_URL = "/static/"

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Make this unique, and don"t share it with anybody.
SECRET_KEY = "1234567890jazzband"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": True,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.admin",

    "oauth2_provider",
    "tests",
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "oauth2_provider": {
            "handlers": ["null"],
            "level": "DEBUG",
            "propagate": True,
        },
    }
}

OAUTH2_PROVIDER = {
    "OIDC_ISS_ENDPOINT": "http://localhost",
    "OIDC_USERINFO_ENDPOINT": "http://localhost/userinfo/",
    "OIDC_RSA_PRIVATE_KEY": "-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQCbCYh5h2NmQuBqVO6G+/CO+cHm9VBzsb0MeA6bbQfDnbhstVOT\nj0hcnZJzDjYc6ajBZZf6gxVP9xrdm9Uh599VI3X5PFXLbMHrmzTAMzCGIyg+/fnP\n0gocYxmCX2+XKyj/Zvt1pUX8VAN2AhrJSfxNDKUHERTVEV9bRBJg4F0C3wIDAQAB\nAoGAP+i4nNw+Ec/8oWh8YSFm4xE6qKG0NdTtSMAOyWwy+KTB+vHuT1QPsLn1vj77\n+IQrX/moogg6F1oV9YdA3vat3U7rwt1sBGsRrLhA+Spp9WEQtglguNo4+QfVo2ju\nYBa2rG+h75qjiA3xnU//F3rvwnAsOWv0NUVdVeguyR+u6okCQQDBUmgWeH2WHmUn\n2nLNCz+9wj28rqhfOr9Ptem2gqk+ywJmuIr4Y5S1OdavOr2UZxOcEwncJ/MLVYQq\nMH+x4V5HAkEAzU2GMR5OdVLcxfVTjzuIC76paoHVWnLibd1cdANpPmE6SM+pf5el\nfVSwuH9Fmlizu8GiPCxbJUoXB/J1tGEKqQJBALhClEU+qOzpoZ6/voYi/6kdN3zc\nuEy0EN6n09AKb8gS9QH1STgAqh+ltjMkeMe3C2DKYK5/QU9/Pc58lWl1FkcCQG67\nZamQgxjcvJ85FvymS1aqW45KwNysIlzHjFo2jMlMf7dN6kobbPMQftDENLJvLWIT\nqoFyGycdsxZiPAIyZSECQQCZFn3Dl6hnJxWZH8Fsa9hj79kZ/WVkIXGmtdgt0fNr\ndTnvCVtA59ne4LEVie/PMH/odQWY0SxVm/76uBZv/1vY\n-----END RSA PRIVATE KEY-----"
}
