
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name='index'),
    path("add_user",views.add_user,name="add_user"),
    path("upload_file",views.upload_xlsfile,name="upload_file"),
    path("form_view",views.form_view,name="form_view"),
    path("sucess",views.sucess,name="sucess"),
    path("Associatexls",views.Associatexls,name="Associatexls"),
    path("leave1",views.leave1,name="leave1"),
]