# Generated by Django 5.0 on 2023-12-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcreated',
            name='not_completed',
        ),
        migrations.AlterField(
            model_name='taskcreated',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
