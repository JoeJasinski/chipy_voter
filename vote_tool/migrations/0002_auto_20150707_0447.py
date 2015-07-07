# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote_tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votingtopic',
            name='slug',
            field=models.SlugField(unique=True, max_length=64),
        ),
    ]
