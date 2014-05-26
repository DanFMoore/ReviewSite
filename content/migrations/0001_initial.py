# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('html_title', models.CharField(max_length=200)),
                ('meta_desc', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('html_title', models.CharField(max_length=200)),
                ('meta_desc', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('menu', models.ForeignKey(to_field='id', to='content.Menu')),
                ('page', models.ForeignKey(null=True, blank=True, to_field='id', to='content.Page')),
                ('static_url', models.CharField(max_length=200, blank=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
    ]
