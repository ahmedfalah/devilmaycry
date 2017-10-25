# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stage1', '0002_auto_20170916_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage1',
            name='mobile_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
