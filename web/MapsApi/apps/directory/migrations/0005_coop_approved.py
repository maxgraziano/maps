# Generated by Django 3.2 on 2021-11-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_auto_20200611_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='coop',
            name='approved',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
