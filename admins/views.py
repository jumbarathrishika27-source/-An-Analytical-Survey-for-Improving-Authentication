
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from users.models import UserRegistrationModel, UserFilesModel

def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid.lower() == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.error(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})

def AdminHome(request):
    return render(request, 'admins/AdminHome.html')

def ViewRegisteredUsers(request):
    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/RegisteredUsers.html', {'data': data})

def AdminActivaUsers(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        try:
            user = UserRegistrationModel.objects.get(id=uid)
            user.status = 'activated'
            user.save()
            messages.success(request, f'User {user.loginid} has been activated successfully')
        except UserRegistrationModel.DoesNotExist:
            messages.error(request, 'User not found')
        except Exception as e:
            messages.error(request, f'Error activating user: {str(e)}')
    return ViewRegisteredUsers(request)

def AdminDeactivateUsers(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        try:
            user = UserRegistrationModel.objects.get(id=uid)
            user.status = 'deactivated'
            user.save()
            messages.success(request, f'User {user.loginid} has been deactivated successfully')
        except UserRegistrationModel.DoesNotExist:
            messages.error(request, 'User not found')
        except Exception as e:
            messages.error(request, f'Error deactivating user: {str(e)}')
    return ViewRegisteredUsers(request)

def UploadedFiles(request):
    data = UserFilesModel.objects.all()
    return render(request, "admins/viewUploadedFiles.html", {"data": data})
