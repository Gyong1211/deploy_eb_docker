from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL='/media/'

WSGI_APPLICATION = 'config.wsgi.deploy.application'

DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

DATABASES = config_secret_deploy['django']['database']

print('@@@@@@@@@@@@@@@@@@@@@@@@ DEBUG:', DEBUG)
print('@@@@@@@@@@@@@@@@@@@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)
