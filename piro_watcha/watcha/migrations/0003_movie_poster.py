# Generated by Django 2.1 on 2018-08-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcha', '0002_auto_20180804_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='포스터'),
        ),
    ]
