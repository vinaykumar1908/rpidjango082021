# Generated by Django 3.0.8 on 2020-09-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractcomment',
            name='commentfile',
            field=models.FileField(blank=True, null=True, upload_to='uploadscontractcomment/%Y/%m/%d/'),
        ),
    ]
