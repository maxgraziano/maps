# Generated by Django 3.2.24 on 2024-03-25 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('directory', '0030_auto_20240322_1922'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoopAddressTags',
            new_name='CoopAddressTagsOld',
        ),
        migrations.RenameModel(
            old_name='Coop',
            new_name='CoopOld',
        ),
        migrations.RenameModel(
            old_name='Person',
            new_name='PersonOld',
        ),
        migrations.AlterField(
            model_name='coopx',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('PROPOSAL', 'Proposal'), ('ARCHIVED', 'Archived')], default='ACTIVE', max_length=8),
        ),
    ]
