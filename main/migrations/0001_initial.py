# Generated by Django 4.2.3 on 2024-11-28 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.TextField()),
                ('creator', models.CharField(max_length=100)),
                ('uuid', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=70, null=True)),
                ('code', models.CharField(max_length=50)),
                ('open', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.option')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.poll')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.poll'),
        ),
    ]
