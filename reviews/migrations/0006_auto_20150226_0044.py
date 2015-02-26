# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='logo',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attribute',
            name='site',
            field=models.ForeignKey(related_name='attributes', to='reviews.Site'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='con',
            name='site',
            field=models.ForeignKey(related_name='cons', to='reviews.Site'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='site',
            field=models.ForeignKey(related_name='offers', to='reviews.Site'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pro',
            name='site',
            field=models.ForeignKey(related_name='pros', to='reviews.Site'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='deposit_options',
            field=models.ManyToManyField(to='reviews.PaymentOption', related_name='deposit_options'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='operator',
            field=models.ForeignKey(related_name='sites', to='reviews.Operator'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='withdrawal_options',
            field=models.ManyToManyField(to='reviews.PaymentOption', related_name='withdrawal_options'),
            preserve_default=True,
        ),
    ]
