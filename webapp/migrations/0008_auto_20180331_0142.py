# Generated by Django 2.0.3 on 2018-03-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20180331_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='Loss',
            new_name='ValueCut',
        ),
        migrations.AlterField(
            model_name='machines',
            name='Enable',
            field=models.IntegerField(),
        ),
    ]
