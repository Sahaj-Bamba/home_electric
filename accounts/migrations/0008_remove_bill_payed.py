# Generated by Django 2.2.3 on 2019-07-10 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_bill_payed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='payed',
        ),
    ]