# Generated by Django 2.0.7 on 2018-08-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcha', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='댓글'),
        ),
    ]
