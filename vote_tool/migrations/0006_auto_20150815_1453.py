# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote_tool', '0005_votingtopic_submission_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votingtopic',
            name='submission_information',
            field=models.TextField(help_text='Information to provide to Choice submitters.', null=True, blank=True),
        ),
    ]
