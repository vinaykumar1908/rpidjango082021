# Generated by Django 3.0.8 on 2020-08-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0010_auto_20200809_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstockdispatchedroh',
            name='Item',
            field=models.CharField(max_length=100),
        ),
    ]
