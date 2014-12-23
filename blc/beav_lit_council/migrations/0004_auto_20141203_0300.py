# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beav_lit_council', '0003_auto_20141203_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.ForeignKey(blank=True, to='beav_lit_council.ContactPref', null=True),
            preserve_default=True,
        ),
    ]
