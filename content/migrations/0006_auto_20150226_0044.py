# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20140524_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(null=True, related_name='children', blank=True, to='content.Menu'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menulink',
            name='menu',
            field=models.ForeignKey(related_name='links', to='content.Menu'),
            preserve_default=True,
        ),
    ]
