# Generated by Django 3.2.6 on 2022-01-12 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_task_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='author',
            new_name='user',
        ),
    ]