# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote_tool', '0003_votingtopic_require_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='votechoice',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='votechoice',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='votingtopic',
            name='require_approval',
            field=models.BooleanField(default=True, verbose_name=b'Submission Require Approval'),
        ),
    ]
