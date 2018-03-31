# Generated by Django 2.0.3 on 2018-03-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20180331_0157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machines',
            name='TokenNo',
        ),
        migrations.AddField(
            model_name='machines',
            name='GrainTypTOkene',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='machines',
            name='StackNo',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
