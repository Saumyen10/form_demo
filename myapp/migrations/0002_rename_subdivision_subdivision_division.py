# Generated by Django 4.2.2 on 2023-07-14 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subdivision',
            old_name='subdivision',
            new_name='division',
        ),
    ]
