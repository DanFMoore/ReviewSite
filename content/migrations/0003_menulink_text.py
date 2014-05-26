# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_menu_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulink',
            name='text',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
