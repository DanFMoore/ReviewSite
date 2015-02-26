# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20150226_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='logo',
            field=models.ImageField(upload_to='/sites/logos/', blank=True, null=True),
            preserve_default=True,
        ),
    ]
