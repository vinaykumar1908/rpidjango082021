# Generated by Django 3.0.6 on 2020-08-10 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidingz', '0004_auto_20200810_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulerecieved',
            name='ModulePresentPosition',
            field=models.CharField(choices=[('TKD_ACTL', 'TKD_ACTL'), ('TKD_HTPP_PWL', 'TKD_HTPP_PWL'), ('ICD_TKD', 'ICD_TKD'), ('TKD_YARD', 'TKD_YARD'), ('SSB_ICD_GHH', 'SSB_ICD_GHH'), ('SSB_ICD_PT', 'SSB_ICD_PT'), ('ICD_NOLI', 'ICD_NOLI'), ('ICD_MUZ', 'ICD_MUZ'), ('BMDJ', 'BMDJ'), ('PCWD_DWNA', 'PCWD_DWNA')], default='YARD', max_length=12),
        ),
    ]