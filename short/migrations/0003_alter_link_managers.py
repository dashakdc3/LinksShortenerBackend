# Generated by Django 4.0.6 on 2022-07-08 09:48

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0002_delete_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='link',
            managers=[
                ('func', django.db.models.manager.Manager()),
            ],
        ),
    ]
