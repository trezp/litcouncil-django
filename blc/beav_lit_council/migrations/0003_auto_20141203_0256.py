# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beav_lit_council', '0002_auto_20141126_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpref',
            name='display_name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contactpref',
            name='short_name',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
