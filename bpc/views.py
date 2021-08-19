from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from stores import models as SM
from sidingz import models as ZM
from django.urls import reverse_lazy
from django.db import models
from bpc import models as bm
import math
from datetime import date, datetime
from home import models as HM
from itertools import filterfalse
#from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from bpc.forms import ModelForm, ModuleDefectForm, ModuleRecieved, ModuleRecievedForm, MRS


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'bpc/bpchome.html'


@login_required
def Enter_BPC(request):
    x = 1
    if request.method == 'POST':
        print(request.POST)
        form = ModuleRecievedForm(request.POST)
        if form.is_valid():
            RakeNumber0 = form.cleaned_data.get('RakeNumber', None)
            BPC_Number = form.cleaned_data.get('BPC_Number', None)

            ModulePresentPosition = form.cleaned_data.get(
                'ModulePresentPosition', None)

            ModuleName = form.cleaned_data.get('ModuleName', None)

            ModuleROHDate = form.cleaned_data.get('ModuleROHDate', None)

            ROHStation = form.cleaned_data.get('ROHStation', None)
            LineNumber = form.cleaned_data.get('LineNumber', None)

            Wagon1Number = form.cleaned_data.get('Wagon1Number', None)

            Wagon1Type = form.cleaned_data.get('Wagon1Type', None)
            Wagon2Number = form.cleaned_data.get('Wagon2Number', None)

            Wagon2Type = form.cleaned_data.get('Wagon2Type', None)
            Wagon3Number = form.cleaned_data.get('Wagon3Number', None)

            Wagon3Type = form.cleaned_data.get('Wagon3Type', None)
            Wagon4Number = form.cleaned_data.get('Wagon4Number', None)

            Wagon4Type = form.cleaned_data.get('Wagon4Type', None)
            Wagon5Number = form.cleaned_data.get('Wagon5Number', None)

            Wagon5Type = form.cleaned_data.get('Wagon5Type', None)
            Wagon1Defect = form.cleaned_data.get('Wagon1Defect', None)
            Wagon2Defect = form.cleaned_data.get('Wagon2Defect', None)
            Wagon3Defect = form.cleaned_data.get('Wagon3Defect', None)
            Wagon4Defect = form.cleaned_data.get('Wagon4Defect', None)
            Wagon5Defect = form.cleaned_data.get('Wagon5Defect', None)
            ModuleRecieveDate = form.cleaned_data.get(
                'ModuleRecieveDate', None)

            stockRecieved = form.cleaned_data.get('stockRecieved', None)
            ModuleDVS = form.cleaned_data.get('ModuleDVS', None)
            ModuleDVR = form.cleaned_data.get('ModuleDVR', None)
            ModuleMadeFit = form.cleaned_data.get('ModuleMadeFit', None)
            author = request.user
            print(Wagon1Defect)
            print(Wagon2Defect)
            print(Wagon3Defect)
            print(Wagon4Defect)
            print(Wagon5Defect)
            print(ModuleDVS)
            print(ModuleDVR)
            print(ModuleMadeFit)
            if ModuleDVS == True:
                MDVS = True
                print("MDVS")
                print(MDVS)
            else:
                MDVS = False
                print("MDVS")
                print(MDVS)

            if ModuleDVR == True:
                MDVR = True
                print("MDVR")
                print(MDVR)
            else:
                MDVR = False
                print("MDVR")
                print(MDVR)

            if ModuleMadeFit == True:
                MMF = True
                print("MMF")
                print(MMF)
            else:
                MMF = False
                print("MMF")
                print(MMF)
            added = models.ModuleRecieved.objects.create(
                RakeNumber=RakeNumber0, BPC_Number=BPC_Number,
                ModulePresentPosition=ModulePresentPosition,
                LineNumber=LineNumber, ModuleName=ModuleName,
                ModuleROHDate=ModuleROHDate, ROHStation=ROHStation, POHStation='POHStation',
                Wagon1Number=Wagon1Number, Wagon1Type=Wagon1Type,
                Wagon2Number=Wagon2Number, Wagon2Type=Wagon2Type,
                Wagon3Number=Wagon3Number, Wagon3Type=Wagon3Type,
                Wagon4Number=Wagon4Number, Wagon4Type=Wagon4Type,
                Wagon5Number=Wagon5Number, Wagon5Type=Wagon5Type,
                ModuleRecieveDate=ModuleRecieveDate, ModuleDVS=MDVS,
                ModuleDVR=MDVR, ModuleMadeFit=MMF, author=author, Wagon1Defect=Wagon1Defect, Wagon2Defect=Wagon2Defect, Wagon3Defect=Wagon3Defect, Wagon4Defect=Wagon4Defect, Wagon5Defect=Wagon5Defect)

            print(added.ModuleDVS)
            print(added.ModuleDVR)
            print(added.ModuleMadeFit)
            added.save()
            x = 1
            print("GO Through")
        else:
            print("did not GO THROUGH")
            x = 0
    form1 = ModuleRecievedForm()
    if x == 1:
        message = messages.success(request, "Success ")
    elif x == 0:
        message = messages.error(request, "Error ")
    context = {
        'messages': message,
        'form1': form1,
        'ModuleDefectForm': ModuleDefectForm()

    }

    return render(request, 'sidings/ModuleRecieved.html', context)


class Show_BPC(LoginRequiredMixin, ListView):
    model = bm.ModuleRecieved
    template_name = 'sidings/ModulesList.html'
    ordering = ['-Date']
    paginate_by = 50
