# Generated by Django 3.2.8 on 2021-11-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referencies', '0002_auto_20211103_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contragent',
            name='contacts',
            field=models.TextField(blank=True, help_text='Contacts information', verbose_name='Contacts'),
        ),
    ]
