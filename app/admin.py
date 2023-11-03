from django.contrib import admin
from .models import Associate,leave
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Associate)
class associate(ImportExportModelAdmin):
    list_display=["Associate_ID",'Associate_Name',"Project_Name",'Department_Name','PM_ID','PM_Name']

@admin.register(leave)
class Leave(ImportExportModelAdmin):
    list_display=["Emp_num",'Name','Team','Total_Leaves']
