# Generated by Django 2.0.3 on 2018-03-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_machines_loss'),
    ]

    operations = [
        migrations.AddField(
            model_name='machines',
            name='Loss',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
    ]