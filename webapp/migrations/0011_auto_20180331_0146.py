# Generated by Django 2.0.3 on 2018-03-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20180331_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='GrainMoisture',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
