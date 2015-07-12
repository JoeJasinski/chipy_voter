# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote_tool', '0002_votingtopic_vote_headers'),
    ]

    operations = [
        migrations.AddField(
            model_name='votechoice',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='votechoice',
            name='picture',
            field=models.ImageField(null=True, upload_to='votechoices', blank=True),
        ),
    ]
