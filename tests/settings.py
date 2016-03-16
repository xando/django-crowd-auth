SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    "crowd_auth",
    "tests",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

AUTH_CROWD_APPLICATION_USER = 'demo'
AUTH_CROWD_APPLICATION_PASSWORD = 'test'
AUTH_CROWD_SERVER_REST_URI = 'http://localhost:8095/crowd/rest/usermanagement/1/'
