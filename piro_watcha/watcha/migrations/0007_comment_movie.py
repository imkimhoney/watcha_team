# Generated by Django 2.0.7 on 2018-08-10 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watcha', '0006_remove_comment_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, to='watcha.Movie'),
            preserve_default=False,
        ),
    ]