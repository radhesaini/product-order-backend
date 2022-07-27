from django.conf import settings
from datetime import datetime

class PrivateApkStorage():
    location = settings.STATIC_URL
    default_acl = 'private'
    file_overwrite = True

def apk_directory_path(instance, filename):
  # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
  return '{0}/{1}'.format(instance.name, datetime.now())