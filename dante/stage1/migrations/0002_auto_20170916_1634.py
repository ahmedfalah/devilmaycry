# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stage1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage1',
            name='city',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='stage1',
            name='state',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
