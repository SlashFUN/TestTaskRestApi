# Generated by Django 2.2 on 2019-04-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20190406_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='Active', max_length=10),
        ),
    ]
