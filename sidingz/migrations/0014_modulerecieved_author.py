# Generated by Django 3.0.6 on 2020-08-30 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sidingz', '0013_auto_20200827_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulerecieved',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]