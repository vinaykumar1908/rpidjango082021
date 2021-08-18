# Generated by Django 3.0.6 on 2020-09-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidingz', '0014_modulerecieved_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulerecieved',
            name='Wagon1Type',
            field=models.CharField(choices=[('SelectWagon', 'Please Select Wagon Type'), ('BCACBMA', 'BCACBMA'), ('BCACBMB', 'BCACBMB'), ('BCACMA', 'BCACMA'), ('BCACMB', 'BCACMB'), ('BOXN', 'BOXN'), ('BOXNHA', 'BOXNHA'), ('BOXNHS', 'BOXNHS'), ('BOXNCR', 'BOXNCR'), ('BOXNLW', 'BOXNLW'), ('BOXNB', 'BOXNB'), ('BOXNF', 'BOXNF'), ('BOXNG', 'BOXNG'), ('BOY', 'BOY'), ('BOST', 'BOST'), ('BOXNAL', 'BOXNAL'), ('BOSTHS', 'BOSTHS'), ('BOXNHL', 'BOXNHL'), ('BOXNAL', 'BOXNAL'), ('BOXNS', 'BOXNS'), ('BCN', 'BCN'), ('BCNA', 'BCNA'), ('BCNAHS', 'BCNAHS'), ('BCCNR', 'BCCNR'), ('BTPN', 'BTPN'), ('BTPNHS', 'BTPNHS'), ('BTPGLN', 'BTPGLN'), ('BTALN', 'BTALN'), ('BTCS', 'BTCS'), ('BTPH', 'BTPH'), ('BTAP', 'BTAP'), ('BTFLN', 'BTFLN'), ('BRNA', 'BRNA'), ('BRNAHS', 'BRNAHS'), ('BFNS', 'BFNS'), ('BOMN', 'BOMN'), ('BRSTH', 'BRSTH'), ('BFAT', 'BFAT'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BRS', 'BRS'), ('BFU', 'BFU'), ('BRHNEHS', 'BRHNEHS'), ('BCL', 'BCL'), ('BCLA', 'BCLA'), ('BOBYN', 'BOBYN'), ('BOBYNHS', 'BOBYNHS'), ('BOBRN', 'BOBRN'), ('BOBRNHS', 'BOBRNHS'), ('BOBRAL', 'BOBRAL'), ('BOBSN', 'BOBSN'), ('BWTB', 'BWTB'), ('MBWT', 'MBWT'), ('DBKM', 'DBKM'), ('MBWZ', 'MBWZ'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='modulerecieved',
            name='Wagon2Type',
            field=models.CharField(choices=[('SelectWagon', 'Please Select Wagon Type'), ('BCACBMA', 'BCACBMA'), ('BCACBMB', 'BCACBMB'), ('BCACMA', 'BCACMA'), ('BCACMB', 'BCACMB'), ('BOXN', 'BOXN'), ('BOXNHA', 'BOXNHA'), ('BOXNHS', 'BOXNHS'), ('BOXNCR', 'BOXNCR'), ('BOXNLW', 'BOXNLW'), ('BOXNB', 'BOXNB'), ('BOXNF', 'BOXNF'), ('BOXNG', 'BOXNG'), ('BOY', 'BOY'), ('BOST', 'BOST'), ('BOXNAL', 'BOXNAL'), ('BOSTHS', 'BOSTHS'), ('BOXNHL', 'BOXNHL'), ('BOXNAL', 'BOXNAL'), ('BOXNS', 'BOXNS'), ('BCN', 'BCN'), ('BCNA', 'BCNA'), ('BCNAHS', 'BCNAHS'), ('BCCNR', 'BCCNR'), ('BTPN', 'BTPN'), ('BTPNHS', 'BTPNHS'), ('BTPGLN', 'BTPGLN'), ('BTALN', 'BTALN'), ('BTCS', 'BTCS'), ('BTPH', 'BTPH'), ('BTAP', 'BTAP'), ('BTFLN', 'BTFLN'), ('BRNA', 'BRNA'), ('BRNAHS', 'BRNAHS'), ('BFNS', 'BFNS'), ('BOMN', 'BOMN'), ('BRSTH', 'BRSTH'), ('BFAT', 'BFAT'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BRS', 'BRS'), ('BFU', 'BFU'), ('BRHNEHS', 'BRHNEHS'), ('BCL', 'BCL'), ('BCLA', 'BCLA'), ('BOBYN', 'BOBYN'), ('BOBYNHS', 'BOBYNHS'), ('BOBRN', 'BOBRN'), ('BOBRNHS', 'BOBRNHS'), ('BOBRAL', 'BOBRAL'), ('BOBSN', 'BOBSN'), ('BWTB', 'BWTB'), ('MBWT', 'MBWT'), ('DBKM', 'DBKM'), ('MBWZ', 'MBWZ'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='modulerecieved',
            name='Wagon3Type',
            field=models.CharField(choices=[('SelectWagon', 'Please Select Wagon Type'), ('BCACBMA', 'BCACBMA'), ('BCACBMB', 'BCACBMB'), ('BCACMA', 'BCACMA'), ('BCACMB', 'BCACMB'), ('BOXN', 'BOXN'), ('BOXNHA', 'BOXNHA'), ('BOXNHS', 'BOXNHS'), ('BOXNCR', 'BOXNCR'), ('BOXNLW', 'BOXNLW'), ('BOXNB', 'BOXNB'), ('BOXNF', 'BOXNF'), ('BOXNG', 'BOXNG'), ('BOY', 'BOY'), ('BOST', 'BOST'), ('BOXNAL', 'BOXNAL'), ('BOSTHS', 'BOSTHS'), ('BOXNHL', 'BOXNHL'), ('BOXNAL', 'BOXNAL'), ('BOXNS', 'BOXNS'), ('BCN', 'BCN'), ('BCNA', 'BCNA'), ('BCNAHS', 'BCNAHS'), ('BCCNR', 'BCCNR'), ('BTPN', 'BTPN'), ('BTPNHS', 'BTPNHS'), ('BTPGLN', 'BTPGLN'), ('BTALN', 'BTALN'), ('BTCS', 'BTCS'), ('BTPH', 'BTPH'), ('BTAP', 'BTAP'), ('BTFLN', 'BTFLN'), ('BRNA', 'BRNA'), ('BRNAHS', 'BRNAHS'), ('BFNS', 'BFNS'), ('BOMN', 'BOMN'), ('BRSTH', 'BRSTH'), ('BFAT', 'BFAT'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BRS', 'BRS'), ('BFU', 'BFU'), ('BRHNEHS', 'BRHNEHS'), ('BCL', 'BCL'), ('BCLA', 'BCLA'), ('BOBYN', 'BOBYN'), ('BOBYNHS', 'BOBYNHS'), ('BOBRN', 'BOBRN'), ('BOBRNHS', 'BOBRNHS'), ('BOBRAL', 'BOBRAL'), ('BOBSN', 'BOBSN'), ('BWTB', 'BWTB'), ('MBWT', 'MBWT'), ('DBKM', 'DBKM'), ('MBWZ', 'MBWZ'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='modulerecieved',
            name='Wagon4Type',
            field=models.CharField(choices=[('SelectWagon', 'Please Select Wagon Type'), ('BCACBMA', 'BCACBMA'), ('BCACBMB', 'BCACBMB'), ('BCACMA', 'BCACMA'), ('BCACMB', 'BCACMB'), ('BOXN', 'BOXN'), ('BOXNHA', 'BOXNHA'), ('BOXNHS', 'BOXNHS'), ('BOXNCR', 'BOXNCR'), ('BOXNLW', 'BOXNLW'), ('BOXNB', 'BOXNB'), ('BOXNF', 'BOXNF'), ('BOXNG', 'BOXNG'), ('BOY', 'BOY'), ('BOST', 'BOST'), ('BOXNAL', 'BOXNAL'), ('BOSTHS', 'BOSTHS'), ('BOXNHL', 'BOXNHL'), ('BOXNAL', 'BOXNAL'), ('BOXNS', 'BOXNS'), ('BCN', 'BCN'), ('BCNA', 'BCNA'), ('BCNAHS', 'BCNAHS'), ('BCCNR', 'BCCNR'), ('BTPN', 'BTPN'), ('BTPNHS', 'BTPNHS'), ('BTPGLN', 'BTPGLN'), ('BTALN', 'BTALN'), ('BTCS', 'BTCS'), ('BTPH', 'BTPH'), ('BTAP', 'BTAP'), ('BTFLN', 'BTFLN'), ('BRNA', 'BRNA'), ('BRNAHS', 'BRNAHS'), ('BFNS', 'BFNS'), ('BOMN', 'BOMN'), ('BRSTH', 'BRSTH'), ('BFAT', 'BFAT'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BRS', 'BRS'), ('BFU', 'BFU'), ('BRHNEHS', 'BRHNEHS'), ('BCL', 'BCL'), ('BCLA', 'BCLA'), ('BOBYN', 'BOBYN'), ('BOBYNHS', 'BOBYNHS'), ('BOBRN', 'BOBRN'), ('BOBRNHS', 'BOBRNHS'), ('BOBRAL', 'BOBRAL'), ('BOBSN', 'BOBSN'), ('BWTB', 'BWTB'), ('MBWT', 'MBWT'), ('DBKM', 'DBKM'), ('MBWZ', 'MBWZ'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='modulerecieved',
            name='Wagon5Type',
            field=models.CharField(choices=[('SelectWagon', 'Please Select Wagon Type'), ('BCACBMA', 'BCACBMA'), ('BCACBMB', 'BCACBMB'), ('BCACMA', 'BCACMA'), ('BCACMB', 'BCACMB'), ('BOXN', 'BOXN'), ('BOXNHA', 'BOXNHA'), ('BOXNHS', 'BOXNHS'), ('BOXNCR', 'BOXNCR'), ('BOXNLW', 'BOXNLW'), ('BOXNB', 'BOXNB'), ('BOXNF', 'BOXNF'), ('BOXNG', 'BOXNG'), ('BOY', 'BOY'), ('BOST', 'BOST'), ('BOXNAL', 'BOXNAL'), ('BOSTHS', 'BOSTHS'), ('BOXNHL', 'BOXNHL'), ('BOXNAL', 'BOXNAL'), ('BOXNS', 'BOXNS'), ('BCN', 'BCN'), ('BCNA', 'BCNA'), ('BCNAHS', 'BCNAHS'), ('BCCNR', 'BCCNR'), ('BTPN', 'BTPN'), ('BTPNHS', 'BTPNHS'), ('BTPGLN', 'BTPGLN'), ('BTALN', 'BTALN'), ('BTCS', 'BTCS'), ('BTPH', 'BTPH'), ('BTAP', 'BTAP'), ('BTFLN', 'BTFLN'), ('BRNA', 'BRNA'), ('BRNAHS', 'BRNAHS'), ('BFNS', 'BFNS'), ('BOMN', 'BOMN'), ('BRSTH', 'BRSTH'), ('BFAT', 'BFAT'), ('BLCA', 'BLCA'), ('BLCB', 'BLCB'), ('BLLA', 'BLLA'), ('BLLB', 'BLLB'), ('BRS', 'BRS'), ('BFU', 'BFU'), ('BRHNEHS', 'BRHNEHS'), ('BCL', 'BCL'), ('BCLA', 'BCLA'), ('BOBYN', 'BOBYN'), ('BOBYNHS', 'BOBYNHS'), ('BOBRN', 'BOBRN'), ('BOBRNHS', 'BOBRNHS'), ('BOBRAL', 'BOBRAL'), ('BOBSN', 'BOBSN'), ('BWTB', 'BWTB'), ('MBWT', 'MBWT'), ('DBKM', 'DBKM'), ('MBWZ', 'MBWZ'), ('BVZC', 'BVZC'), ('BVZI', 'BVZI'), ('BFKHN', 'BFKHN')], default='SelectWagon', max_length=11, null=True),
        ),
    ]