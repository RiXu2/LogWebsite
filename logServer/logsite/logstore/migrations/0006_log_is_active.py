# Generated by Django 3.1.1 on 2021-05-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logstore', '0005_auto_20210506_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Delete'),
        ),
    ]
