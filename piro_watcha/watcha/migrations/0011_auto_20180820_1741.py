# Generated by Django 2.1 on 2018-08-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcha', '0010_auto_20180820_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='movie_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='영화 제목'),
        ),
    ]