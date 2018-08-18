# Generated by Django 2.1 on 2018-08-18 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watcha', '0005_auto_20180812_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='movie',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='영화 제목'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='이 작품에 대한 생각을 자유롭게 표현해주세요.'),
        ),
    ]
