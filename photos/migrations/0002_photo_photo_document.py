# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_document',
            field=models.FileField(null=True, upload_to=b'normal/photos/%y/%m/%d/', blank=True),
        ),
    ]
