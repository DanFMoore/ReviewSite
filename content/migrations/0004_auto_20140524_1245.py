# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_menulink_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulink',
            name='content_type',
            field=models.ForeignKey(null=True, blank=True, to_field='id', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menulink',
            name='object_id',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='menulink',
            name='page',
        ),
    ]
