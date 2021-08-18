from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from twilio.rest import Client
# Create your models here.


class ModuleRecieved(models.Model):
    WAGON_TYPE_CHOICES = (
        ("SelectWagon", "Please Select Wagon Type"),
        ("BOXN", "BOXN"),
        ("BOXNHA", "BOXNHA"),
        ("BOXNHS", "BOXNHS"),
        ("BOXNCR", "BOXNCR"),
        ("BOXNLW", "BOXNLW"),
        ("BOXNB", "BOXNB"),
        ("BOXNF", "BOXNF"),
        ("BOXNG", "BOXNG"),
        ("BOY", "BOY"),
        ("BOST", "BOST"),
        ("BOXNAL", "BOXNAL"),
        ("BOSTHS", "BOSTHS"),
        ("BOXNHL", "BOXNHL"),
        ("BOXNAL", "BOXNAL"),
        ("BOXNS", "BOXNS"),
        ("BCN", "BCN"),
        ("BCNA", "BCNA"),
        ("BCNAHS", "BCNAHS"),
        ("BCCNR", "BCCNR"),
        ("BTPN", "BTPN"),
        ("BTPNHS", "BTPNHS"),
        ("BTPGLN", "BTPGLN"),
        ("BTALN", "BTALN"),
        ("BTCS", "BTCS"),
        ("BTPH", "BTPH"),
        ("BTAP", "BTAP"),
        ("BTFLN", "BTFLN"),
        ("BRNA", "BRNA"),
        ("BRNAHS", "BRNAHS"),
        ("BFNS", "BFNS"),
        ("BOMN", "BOMN"),
        ("BRSTH", "BRSTH"),
        ("BFAT", "BFAT"),
        ("BLCA", "BLCA"),
        ("BLCB", "BLCB"),
        ("BLLA", "BLLA"),
        ("BLLB", "BLLB"),
        ("BRS", "BRS"),
        ("BFU", "BFU"),
        ("BRHNEHS", "BRHNEHS"),
        ("BCL", "BCL"),
        ("BCLA", "BCLA"),
        ("BOBYN", "BOBYN"),
        ("BOBYNHS", "BOBYNHS"),
        ("BOBRN", "BOBRN"),
        ("BOBRNHS", "BOBRNHS"),
        ("BOBRAL", "BOBRAL"),
        ("BOBSN", "BOBSN"),
        ("BWTB", "BWTB"),
        ("MBWT", "MBWT"),
        ("DBKM", "DBKM"),
        ("MBWZ", "MBWZ"),
        ("BVZC", "BVZC"),
        ("BVZI", "BVZI"),
        ("BFKHN", "BFKHN"),
    )
    TypeOfBPC = (
        ("Exam", "Please Select Examination Line"),
        ("End to End", "End to End"),
        ("Intensive", "Intensive"),
        ("Closed Circuit", "Closed Circuit"),
    )
    Serial = models.AutoField(primary_key=True)
    Date = models.DateTimeField(default=timezone.now)
    TrainNo = models.CharField(max_length=50, null=True, blank=True)
    TypeOfExamination = models.CharField(max_length=10, choices=TypeOfBPC, default='Exam', null=True, blank=False)
    BPC_Number = models.BigIntegerField(null=True, blank=False)
    BPCDate = models.DateField(null=True, blank=False)
    RakeID: models.CharField(max_length = 100, null = True, blank = False)
    LocoNo: models.IntegerField(max_length=5, null=True, blank=False)
    LoadnStock : models.CharField(max_length=10, null=True, blank=False)
    TotalBreakCylinders : models.IntegerField(max_length=3, null=True, blank=False)
    OperatingCylinders : models.IntegerField(max_length=3, null=True,blank=False)
    BreakPower : models.IntegerField(max_length=2, null=True, blank=False)
    BPLoco: models.FloatField(null=True, blank=False)
    BPBV: models.FloatField(null=True, blank=False)
    FPLoco: models.FloatField(null=True, blank=True)
    FPBV: models.FloatField(null=True, blank=True)
    EOT: models.TimeField()
    APReadyTime: models.TimeField()
    Wagon1Number = models.BigIntegerField(null=True, blank=True)
    TypeOfExamination = models.CharField(max_length=10, null=True, blank=False)

    Wagon1Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon2Number = models.BigIntegerField(null=True, blank=True)
    Wagon2Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon3Number = models.BigIntegerField(null=True, blank=True)
    Wagon3Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon4Number = models.BigIntegerField(null=True, blank=True)
    Wagon4Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    Wagon5Number = models.BigIntegerField(null=True, blank=True)
    Wagon5Type = models.CharField(
        max_length=11, choices=WAGON_TYPE_CHOICES, default='SelectWagon', null=True, blank=True)
    ModuleRecieveDate = models.DateField(null=True, default='1001-01-01')
    ModuleCommDate = models.DateField(
        null=True, default='1001-01-01', blank=True)
    ModuleROHDate = models.DateField(
        null=True, default='1001-01-01', blank=True)
    ModulePOHDate = models.DateField(
        null=True, default='1001-01-01', blank=True)
    Wagon1Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon2Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon3Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon4Defect = models.CharField(
        max_length=100, null=True, blank=True)
    Wagon5Defect = models.CharField(
        max_length=100, null=True, blank=True)
    ModuleDVS = models.BooleanField(default=False, blank=True)
    ModuleDVR = models.BooleanField(default=False, blank=True)
    ModuleDVSDate = models.DateField(null=True, blank=True)
    POHStation = models.CharField(max_length=100, null=True, blank=True)
    ROHStation = models.CharField(max_length=100, null=True, blank=True)
    ModuleMadeFit = models.BooleanField(default=False, blank=True)
    ModuleMadeFitDateTime = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ROHFile = models.FileField(
        upload_to='ROH/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return str(self.ModuleName)

    def get_absolute_url(self):
        return reverse('Modules_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        account_sid = "AC7df1d3a6422280115a2a3fa0c0139b30"
        # Your Auth Token from twilio.com/console
        auth_token = "6bc2c95d10be56efa219fff586689c07"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+919717631424",
            from_="+15674323089",
            body=f'Module Name: {self.ModuleName}; Type: {self.Wagon1Type}; DVS: {self.ModuleDVS}; DVR: {self.ModuleDVR}; SSE: {self.author}')

        print(message.sid)
        print("Module Saved !")
        return super().save(*args, **kwargs)
