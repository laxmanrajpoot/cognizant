# Create your views here.
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import pandas as pd
from openpyxl import load_workbook
from .models import *
from django.contrib import messages
import django_tables2 as tables

def index(request):
    return render(request,"index.html")

def add_user(request):
    return render(request,"form.html")

def upload_xlsfile(request):
    return render(request,"upload_file.html")

def sucess(request):
    return render(request,"sucess.html")

#Associate data form
def form_view(request):
    try:
        if request.method=='POST':
            Sdepartment=request.POST.get('Sdepartment')
            Avm=request.POST.get("Avm")
            Associate_id=request.POST.get('Associate_id')
            Name=request.POST.get('Name')
            Grade=request.POST.get('Grade')
            Bu=request.POST.get('Bu')
            Project_id=request.POST.get('Project_id')
            Project_name=request.POST.get('Project_name')
            Classification=request.POST.get('Classification')
            Pm_id=request.POST.get('Pm_id')
            Pm_name=request.POST.get('Pm_name')
            Account_id=request.POST.get('Account_id')
            Account_name=request.POST.get('Account_name')
            Customer_id=request.POST.get('Customer_id')
            Parent_cus=request.POST.get('Parent_cus')
            Ptag=request.POST.get('Ptag')
            Stag=request.POST.get('Stag')
            Hm_id=request.POST.get('Hm_id')
            Billability=request.POST.get('Billability')
            Country=request.POST.get('Country')
            State=request.POST.get('State')
            City=request.POST.get('City')
            Office_loc=request.POST.get('Office_loc')
            Ons_off=request.POST.get('Ons_off')
            Start_date=request.POST.get('Start_date')
            End_date=request.POST.get('End_date')
            Assignment_status=request.POST.get('Assignment_status')
            Percent_all=request.POST.get('Percent_all')
            Department=request.POST.get('Department')
            Vertical=request.POST.get('Vertical')
            Pstart_date=request.POST.get('Pstart_date')
            Pend_date=request.POST.get('Pend_date')
            Market_na=request.POST.get('Market_na')
            Market=request.POST.get('Market')
            Market_unit=request.POST.get('Market_unit')
            Poll_id=request.POST.get('Poll_id')
            if Associate.objects.filter(Associate_ID=Associate_id).count()>0:
                return HttpResponse("Details Already Exists")
            else:
                s=Associate(Sub_department=Sdepartment,AIA_Avm=Avm,Associate_ID=Associate_id,Associate_Name=Name,Grade=Grade,
                            Bu_Classified=Bu, Project_ID=Project_id,Project_Name=Project_name,Grid_Classification=Classification,
                            PM_ID=Pm_id,PM_Name=Pm_name,Account_ID=Account_id,Account_Name=Account_name,Parent_Customer_ID=Customer_id,
                            Parent_Customer=Parent_cus,Primary_Tag=Ptag, Secondary_Tag=Stag, Home_Manager_ID=Hm_id, Billability_Status=Billability,
                            Country=Country,State=State,City=City,Location_Description=Office_loc,Ons_off=Ons_off, Assignment_Start_Date=Start_date,
                            Assignment_End_Date=End_date,Assignment_Status=Assignment_status, Percent_Allocation=Percent_all,
                            Department_Name=Department, Sub_Vertical=Vertical,Project_Start_Date=Pstart_date,Project_End_Date=Pend_date,
                            Market_Na_GGM_Classified=Market_na,Market=Market,Market_Unit=Market_unit,Poll_ID=Poll_id
                            
                            )
                s.save()
                messages.success(request,"Data Saved Sucessfully")
    except:
        pass
    return render(request,"form.html")


#Associate file upload 
def create_df(file_path):
    df=pd.read_excel(file_path)
    print(df)


def Associatexls(request):
    try:
        if request.method== "POST":
            file=request.FILES['file1']
            obj=File.objects.create(file=file)
            create_df(obj.file)
    except:
        pass
    return render(request,"upload_file.html")

def leave1(request):
    try:
        if request.method=="POST":
            Team=request.POST.get('Team')
            Associate_id=request.POST.get('Associate_id')
            Name=request.POST.get('Name')
            Jan=request.POST.get('Jan')
            Feb=request.POST.get('Feb')
            Mar=request.POST.get('Mar')
            Apr=request.POST.get('Apr')
            May=request.POST.get('May')
            Jun=request.POST.get('Jun')
            Jul=request.POST.get('Jul')
            Aug=request.POST.get('Aug')
            Sep=request.POST.get('Sep')
            Oct=request.POST.get('Oct')
            Nov=request.POST.get('Nov')
            Dec=request.POST.get('Dec')
           
            Total=(int(Jan)+int(Feb)+int(Mar)+int(Apr)+int(May)+int(Jun)+int(Jul)+int(Sep)+int(Oct)+int(Nov)+int(Dec))
            s1=leave(Team=Team,Emp_num=Associate_id,Name=Name,Jan=Jan,Feb=Feb,Mar=Mar,Apr=Apr,May=May,Jun=Jun,
                        Jul=Jul,Aug=Aug,Sep=Sep,Oct=Oct,Nov=Nov,Dec=Dec,Total=Total)
            s1.save()
            messages.success(request,"Data Saved Sucessfully")
                
    except:
        pass
    return render(request,"leave_form.html")


