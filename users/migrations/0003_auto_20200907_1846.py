# Generated by Django 3.0.8 on 2020-09-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200905_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='LocalAddress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Mobile',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
