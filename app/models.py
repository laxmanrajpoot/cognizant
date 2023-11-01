from django.db import models

# Create your models here.
class Associate(models.Model):
    Sub_department=models.CharField(max_length=50)
    AIA_Avm=models.CharField(max_length=50)
    Associate_ID=models.IntegerField()
    Associate_Name=models.CharField(max_length=25)
    Grade=models.CharField(max_length=10)
    Bu_Classified=models.CharField(max_length=25)
    Project_ID=models.IntegerField()
    Project_Name=models.CharField(max_length=50)
    Grid_Classification=models.CharField(max_length=25)
    PM_ID=models.IntegerField()
    PM_Name=models.CharField(max_length=25)
    Account_ID=models.IntegerField()
    Account_Name=models.CharField(max_length=25)
    Parent_Customer_ID=models.IntegerField()
    Parent_Customer=models.CharField(max_length=25)
    Primary_Tag=models.CharField(max_length=25)
    Secondary_Tag=models.CharField(max_length=25)
    Home_Manager_ID=models.IntegerField()
    Billability_Status=models.CharField(max_length=10)
    Country=models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    City=models.CharField(max_length=25)
    Location_Description=models.CharField(max_length=25)
    Ons_off=models.CharField(max_length=10)
    Assignment_Start_Date=models.DateField()
    Assignment_End_Date=models.DateField()
    Assignment_Status=models.CharField(max_length=10)
    Percent_Allocation=models.IntegerField()
    Department_Name=models.CharField(max_length=25)
    Sub_Vertical=models.CharField(max_length=25)
    Project_Start_Date=models.DateField()
    Project_End_Date=models.DateField()
    Market_Na_GGM_Classified=models.CharField(max_length=25)
    Market=models.CharField(max_length=25)
    Market_Unit=models.CharField(max_length=25)
    Poll_ID=models.IntegerField(25)

    def __str__(self):
        return self.Associate_Name

class leave(models.Model):
    Team=models.CharField(max_length=20)
    Emp_num=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=25)
    Jan=models.IntegerField(default=0)
    Feb=models.IntegerField(default=0)
    Mar=models.IntegerField(default=0)
    Apr=models.IntegerField(default=0)
    May=models.IntegerField(default=0)
    Jun=models.IntegerField(default=0)
    Jul=models.IntegerField(default=0)
    Aug=models.IntegerField(default=0)
    Sep=models.IntegerField(default=0)
    Oct=models.IntegerField(default=0)
    Nov=models.IntegerField(default=0)
    Dec=models.IntegerField(default=0)
    Total=models.IntegerField(default=0)

    def __str__(self):
        return self.Name
