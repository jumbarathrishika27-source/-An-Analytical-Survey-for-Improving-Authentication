
from django.contrib import admin
from django.urls import path
from AnalyticalCloud import views as mainView
from users import views as usr
from admins import views as admins
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name='index'),
    path("index/", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),

    ### User Side Views
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("qrcodecheck/", usr.qrcodecheck, name="qrcodecheck"),
    path("UserUploadFiles/", usr.UserUploadFiles, name="UserUploadFiles"),
    path("viewUploadedFiles/", usr.viewUploadedFiles, name="viewUploadedFiles"),
    path("download/", usr.download, name="download"),
    path("DecryptFiles/", usr.DecryptFiles, name="DecryptFiles"),
    path("dataDecrypt/", usr.dataDecrypt, name="dataDecrypt"),

    ### Admin Side Views
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("ViewRegisteredUsers/", admins.ViewRegisteredUsers, name="ViewRegisteredUsers"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers"),
    path("AdminDeactivateUsers/", admins.AdminDeactivateUsers, name="AdminDeactivateUsers"),
    path("UploadedFiles/", admins.UploadedFiles, name="UploadedFiles"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)