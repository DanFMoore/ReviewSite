from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.utils.translation import ugettext_lazy as _

FlatPage.url2 = models.CharField(_('URL'), max_length=100, db_index=True)