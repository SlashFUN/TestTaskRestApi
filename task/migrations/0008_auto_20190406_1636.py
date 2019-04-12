# Generated by Django 2.2 on 2019-04-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20190406_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', error_messages={'invalid': 'example@mail.com'}, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Enter username: ', max_length=100, verbose_name='Nickname'),
        ),
    ]
