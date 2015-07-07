# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote_tool', '0002_auto_20150707_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingtopic',
            name='require_approval',
            field=models.BooleanField(default=True),
        ),
    ]
