from django.contrib import admin
from .models import Associate,leave
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Associate)
class associate(ImportExportModelAdmin):
    pass

@admin.register(leave)
class Leave(ImportExportModelAdmin):
    pass

