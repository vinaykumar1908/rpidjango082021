# Generated by Django 3.2.6 on 2021-08-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200813_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
