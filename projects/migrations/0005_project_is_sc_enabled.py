# Generated by Django 3.0.8 on 2020-07-27 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200723_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_sc_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
