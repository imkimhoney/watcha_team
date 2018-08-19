# Generated by Django 2.1 on 2018-08-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcha', '0007_auto_20180819_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='movie_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='영화 제목'),
        ),
    ]