# Generated by Django 3.0.7 on 2020-07-08 04:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import recurrence.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time at which an object was created', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time at which an object was modified', verbose_name='updated_at')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('start_date', models.DateField(default=datetime.date.today, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('is_completed', models.BooleanField(default=False, verbose_name='completed')),
                ('is_paused', models.BooleanField(default=False, verbose_name='paused')),
                ('is_public', models.BooleanField(default=False, verbose_name='public')),
                ('recurrence', recurrence.fields.RecurrenceField()),
                ('total_instances', models.PositiveIntegerField(default=0)),
                ('total_instances_done', models.PositiveIntegerField(default=0)),
                ('completion_rate', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_to_do', models.DateField(default=django.utils.timezone.now, help_text='Date at which an habit must be done', verbose_name='date')),
                ('is_done', models.BooleanField(default=False)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='habits.Habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
