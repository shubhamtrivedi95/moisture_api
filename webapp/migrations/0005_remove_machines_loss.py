# Generated by Django 2.0.3 on 2018-03-30 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180331_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machines',
            name='loss',
        ),
    ]