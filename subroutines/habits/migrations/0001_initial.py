# Generated by Django 3.0.7 on 2020-07-05 02:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('is_completed', models.BooleanField(default=False)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_paused', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('recurrence', models.CharField(max_length=200, verbose_name='recurrence')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
