# Generated by Django 4.2.1 on 2023-06-01 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='Message',
            new_name='messages',
        ),
    ]
