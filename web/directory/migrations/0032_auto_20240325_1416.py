# Generated by Django 3.2.24 on 2024-03-25 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0031_auto_20240325_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coopold',
            name='contact_methods',
        ),
        migrations.RemoveField(
            model_name='coopold',
            name='rec_updated_by',
        ),
        migrations.RemoveField(
            model_name='coopold',
            name='types',
        ),
        migrations.RemoveField(
            model_name='personold',
            name='contact_methods',
        ),
        migrations.RemoveField(
            model_name='personold',
            name='coops',
        ),
        migrations.DeleteModel(
            name='CoopAddressTagsOld',
        ),
        migrations.DeleteModel(
            name='CoopOld',
        ),
        migrations.DeleteModel(
            name='PersonOld',
        ),
    ]
