# Generated by Django 3.2.24 on 2024-03-23 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0029_auto_20240321_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cooppublic',
            name='coop',
        ),
        migrations.AddField(
            model_name='coopx',
            name='coop_public',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directory.cooppublic'),
        ),
        migrations.AddField(
            model_name='coopx',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=8),
        ),
    ]
