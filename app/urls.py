
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name='index'),
    path("add_user",views.add_user,name="add_user"),
    path("upload_file",views.upload_file,name="upload_file"),
    path("sucess",views.sucess,name="sucess"),
    path("leave1",views.leave1,name="leave1"),
    path("upload_file2",views.upload_file2,name='upload_file2'),
    
]
