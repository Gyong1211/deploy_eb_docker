from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

MEDIA_URL='/media/'
STATIC_URL='/static/'

WSGI_APPLICATION = 'config.wsgi.deploy.application'

AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['s3_bucket_name']
AWS_S3_REGION_NAME = config_secret_deploy['aws']['s3_region_name']
S3_USE_SIGV4=True
# AWS_S3_SIGNATURE_VERSION = config_secret_deploy['aws']['s3_signature_version']

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

DATABASES = config_secret_deploy['django']['database']


print('@@@@@@@@@@@@@@@@@@@@@@@@ DEBUG:', DEBUG)
print('@@@@@@@@@@@@@@@@@@@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)
