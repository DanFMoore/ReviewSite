# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('native_name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('html_title', models.CharField(max_length=200)),
                ('meta_desc', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('date_added', models.DateTimeField()),
                ('date_established', models.DateTimeField()),
                ('review', models.TextField()),
                ('affiliate_link', models.CharField(max_length=200)),
                ('visible_link', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('slug', models.SlugField()),
                ('operator', models.ForeignKey(to_field='id', to='reviews.Operator')),
                ('games', models.ManyToManyField(to='reviews.Game')),
                ('languages', models.ManyToManyField(to='reviews.Language')),
                ('deposit_options', models.ManyToManyField(to='reviews.PaymentOption')),
                ('withdrawal_options', models.ManyToManyField(to='reviews.PaymentOption')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
    ]
