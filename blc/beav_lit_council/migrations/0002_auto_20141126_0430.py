# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beav_lit_council', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='announcement',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='title',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
