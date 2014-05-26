# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_con'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('info', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('affiliate_link', models.CharField(max_length=200)),
                ('visible_link', models.CharField(max_length=200)),
                ('site', models.ForeignKey(to_field='id', to='reviews.Site')),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
    ]
