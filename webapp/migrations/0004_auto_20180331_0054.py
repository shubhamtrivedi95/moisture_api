# Generated by Django 2.0.3 on 2018-03-30 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180331_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='Loss',
            new_name='loss',
        ),
    ]
