# Generated by Django 3.0.8 on 2020-08-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidingz', '0002_auto_20200809_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulerecieved',
            name='ModuleDVSDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modulerecieved',
            name='ModuleMadeFitDateTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
