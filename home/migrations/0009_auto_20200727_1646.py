# Generated by Django 3.0.8 on 2020-07-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200726_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='designation',
            field=models.CharField(default='Developer', max_length=100, verbose_name='Designation'),
        ),
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.URLField(blank=True, default='', verbose_name='Url'),
        ),
    ]