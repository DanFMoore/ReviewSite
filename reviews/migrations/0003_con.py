# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_attribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Con',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('site', models.ForeignKey(to_field='id', to='reviews.Site')),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
