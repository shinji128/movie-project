# Generated by Django 3.1.5 on 2021-01-19 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_auto_20210119_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieblog',
            name='user',
            field=models.TextField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]