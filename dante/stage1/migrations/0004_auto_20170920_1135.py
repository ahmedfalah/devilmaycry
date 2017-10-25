# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stage1', '0003_stage1_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage1',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='stage1',
            name='phone_number',
            field=models.CharField(default=0, max_length=13),
            preserve_default=False,
        ),
    ]
