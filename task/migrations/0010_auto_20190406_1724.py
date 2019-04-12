# Generated by Django 2.2 on 2019-04-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20190406_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='create',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='delete',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nickname'),
        ),
    ]