# Generated by Django 3.2.6 on 2022-01-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='task',
            name='time_tobe_completed',
            field=models.DateField(auto_now=True),
        ),
    ]
