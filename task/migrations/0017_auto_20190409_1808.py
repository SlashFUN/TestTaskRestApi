# Generated by Django 2.2 on 2019-04-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_auto_20190407_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.TextField(verbose_name='Name'),
        ),
    ]
