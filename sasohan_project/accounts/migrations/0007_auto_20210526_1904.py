# Generated by Django 3.1.7 on 2021-05-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210526_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=60),
        ),
    ]