# Generated by Django 3.0.7 on 2020-07-10 06:57

from django.db import migrations
import subroutines.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', subroutines.users.models.UserManager()),
            ],
        ),
    ]