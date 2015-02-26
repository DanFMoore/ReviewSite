# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20150226_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='sites/logos/'),
            preserve_default=True,
        ),
    ]
