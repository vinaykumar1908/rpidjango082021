from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from twilio.rest import Client

class Rake(models.Model):
    EXAMINATION_CHOICES = (
        ("SELECTEXAM", "Please Select Examination Line"),
        ("CC", "CC: 7500Km/30Days"),
        ("E2E", "END2END"),
        ("STR", "STR"),
        ("PREMIUM", "PREMIUM"),
    )
    EXAMINATION_PLACE = (
        ("SELECTEXAMPLACE", "Please Select Examination Place"),
        ("TKD_ACTL", "TKD ACTL"),
        ("TKD_HTPP_PWL", "TKD HTPP PWL"),
        ("TKD_ICD", "TKD ICD"),
        ("TKD_YARD", "TKD YARD"),
        ("SSB_ICD_GHH", "SSB ICD GHH"),
        ("SSB_ICD_PT", "SSB ICD PTT"),
        ("GZB_ICD_NOLI", "GZB ICD NOLI"),
        ("GZB_ICD_MUZ", "GZB ICD MUZ"),
        ("PNP_BMDJ", "PNP BMDJ"),
        ("PNP_PCWD_DWNA", "PNP PCWD DWNA"),
    )
    Serial = models.AutoField(primary_key=True)
    RakeName = models.CharField(max_length=100)
    RakeAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    ExamType = models.CharField(
        max_length=10, choices=EXAMINATION_CHOICES, default='SELECTEXAM', null=True, blank=True, required=True)
    ExamPlace = models.CharField(
        max_length=10, choices=EXAMINATION_PLACE, default='SELECTEXAMPLACE', null=True, blank=True, required=True)
    BPCNumber = models.BigIntegerField(null=True, blank=False, required=True)
    RakeID = models.CharField(max_length=50, null=True, required=True)
    TrainNumber = models.CharField(max_length=50, null=True, required=True)
    Load&Stock = models.IntegerField(null=True, blank=True)
    NoOpCyl = models.IntegerField(null=True, blank=True)
    LocoNo = models.IntegerField(null=True, blank=True)
    NoBkCyl = models.IntegerField(null=True, blank=True)
    BkPower = models.IntegerField(null=True, blank=True)
    EOT = models.TimeField(null=True, blank=True)
    APReady = models.TimeField(null=True, blank=True)
    ValidUpto = models.DateField(null=True, default='1001-01-01', blank=True, required=True)
    IssueDate = models.DateField(null=True, default='1001-01-01', blank=True, required=True)

    def __str__(self):
        return self.RakeName

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Module(models.Model):
    RakeName = models.ForeignKey(Rake, on_delete=models.CASCADE, related_name='bmodule')
    ModuleName = models.CharField(max_length=20, null=True)
    approved_comment = models.BooleanField(default=False)
    ModuleROHDate = models.DateField(null=True, default='1001-01-01', blank=True)
    ModulePOHDate = models.DateField(null=True, default='1001-01-01', blank=True)
    POHStation = models.CharField(max_length = 100, null = True, blank = True)
    ROHStation = models.CharField(max_length=100, null=True, blank=True)
    ModuleDVS = models.BooleanField(default=False, blank=True)
    ModuleDVR = models.BooleanField(default=False, blank=True)
    ModuleDVSDate = models.DateField(null=True, blank=True)
    ModuleMadeFit = models.BooleanField(default=False, blank=True)
    ModuleMadeFitDateTime = models.DateTimeField(null=True, blank=True)
    ModuleAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.ModuleName

class Wagon(models.Model):
    ModuleName = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='bwagon')
    WagonNumber = models.IntegerField(blank=True, null=True)
    WagonRepair = models.CharField(max_length=100, null=True, blank=True)
    WagonAuthor = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.WagonNumber