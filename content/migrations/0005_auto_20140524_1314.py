# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20140524_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulink',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
