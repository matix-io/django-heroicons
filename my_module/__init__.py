import base64
import json
import os


def configure(key):
    data = json.loads(base64.b64decode(key))

    global AWS_STORAGE_BUCKET_NAME
    global AWS_ACCESS_KEY_ID
    global AWS_SECRET_ACCESS_KEY
    global AWS_REGION
    global AWS_QUERYSTRING_AUTH
    global AWS_S3_ENCRYPTION
    global AWS_S3_CUSTOM_DOMAIN
    global AWS_S3_SIGNATURE_VERSION
    global AWS_S3_REGION_NAME
    global DEFAULT_FILE_STORAGE
    global MEDIA_ROOT
    global MEDIA_URL

    os.environ['S3_USE_SIGV4'] = 'True'
    AWS_STORAGE_BUCKET_NAME = data.get('AWS_BUCKET_NAME')
    AWS_ACCESS_KEY_ID = data.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = data.get('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = data.get('AWS_REGION')
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_ENCRYPTION = False
    AWS_S3_CUSTOM_DOMAIN = 's3.{}.amazonaws.com/{}'.format(AWS_REGION, AWS_STORAGE_BUCKET_NAME)
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_REGION_NAME = AWS_REGION
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_ROOT = '/'
    MEDIA_URL = '//s3.{}.amazonaws.com/{}/'.format(AWS_REGION, AWS_STORAGE_BUCKET_NAME)
