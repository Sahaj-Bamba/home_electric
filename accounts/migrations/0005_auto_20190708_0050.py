# Generated by Django 2.2.3 on 2019-07-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190708_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='dor',
            field=models.DateTimeField(verbose_name='dor'),
        ),
    ]
