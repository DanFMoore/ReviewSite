# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(null=True, blank=True, to_field='id', to='content.Menu'),
            preserve_default=True,
        ),
    ]
