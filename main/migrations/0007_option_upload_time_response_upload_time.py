# Generated by Django 4.2.3 on 2024-11-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_poll_upload_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]