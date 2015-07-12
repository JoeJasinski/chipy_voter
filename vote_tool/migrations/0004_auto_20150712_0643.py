# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote_tool', '0003_auto_20150711_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='votechoice',
            name='link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='votechoice',
            name='link_text',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
