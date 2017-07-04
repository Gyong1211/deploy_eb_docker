from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

WSGI_APPLICATION = 'config.wsgi.deploy.application'

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

print('@@@@@@@@@@@@@@@@@@@@@@@@ DEBUG:', DEBUG)
print('@@@@@@@@@@@@@@@@@@@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)
