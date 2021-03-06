# Generated by Django 3.0.7 on 2020-07-08 00:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time at which an object was created', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time at which an object was modified', verbose_name='updated_at')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('total_habits', models.PositiveIntegerField(default=0)),
                ('total_habits_today', models.PositiveIntegerField(default=0)),
                ('total_habits_done_today', models.PositiveIntegerField(default=0)),
                ('completion_rate', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('completion_streak', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
