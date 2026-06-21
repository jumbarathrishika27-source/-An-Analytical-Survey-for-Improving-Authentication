
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel,UserFilesModel
from django.conf import settings
from qrcode import *
from django.core.files.storage import FileSystemStorage
from cryptography.fernet import Fernet
import os


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def generateQRCode():
    import random
    fixed_digits = 6
    return random.randrange(111111, 999999, fixed_digits)


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                data = generateQRCode()
                request.session['qrcode'] = data
                print("QR Code is :",data)
                img = make(data)
                img_name = 'qrCodeAlex.png'
                img.save(settings.MEDIA_ROOT + '\\' + img_name)
                # return render(request, 'index.html', )
                return render(request, 'GraphicleAuth.html', {'img_name': img_name})
                # return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your account is not activated or has been deactivated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})

def qrcodecheck(request):
    if request.method=='POST':
        server_qr = request.session['qrcode']
        browser_qr = int(request.POST.get('data'))
        print(f"Server Side QR:{type(server_qr)} Browser Side QR:{type(browser_qr)}")
        if server_qr == browser_qr:
            return render(request, 'users/UserHome.html', {})
        else:
            messages.success(request, 'Invalid QR Code')
            return render(request, 'UserLogin.html', {})
    else:
        return render(request, 'UserLogin.html', {})

def UserHome(request):
    return render(request, 'users/UserHome.html', {})


def UserUploadFiles(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        loc = settings.MEDIA_ROOT + '\\' + 'files'
        fs = FileSystemStorage(loc)
        key = Fernet.generate_key()

        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # string the key in a file
        fileKey = loc+"\\"+filename+".key"
        with open(fileKey, 'wb') as filekey:
            filekey.write(key)
        # opening the key
        with open(fileKey, 'rb') as filekey:
            key = filekey.read()
        print("Encrypt Key:", key)
        fernet = Fernet(key)
        with open(loc+"\\"+filename, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(loc+"\\"+filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        loginid =  request.session['loginid']
        email = request.session['email']
        filepath = os.path.join(loc, filename)
        # UserFilesModel.objects.all().delete()
        UserFilesModel.objects.create(username=loginid,email=email,filename=filename,enckey=fileKey,file=filepath)
        return render(request, "users/uploadfiles.html", {'msg':'Encrypted success'})
    else:
        return render(request, "users/uploadfiles.html", {})


def viewUploadedFiles(request):
    loginid = request.session['loginid']
    data = UserFilesModel.objects.filter(username=loginid)
    response = HttpResponse('text/csv')
    return render(request, "users/viewUploadedFiles.html", {"data": data})

def DecryptFiles(request):
    loginid = request.session['loginid']
    data = UserFilesModel.objects.filter(username=loginid)
    return render(request, "users/usrDecrypts.html", {"data": data})


def download(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse('text/csv')
    fileis = request.GET.get('fileis')
    response['Content-Disposition'] = f'attachment; filename={fileis}'
    # Create the CSV writer using the HttpResponse as the "file"
    return response


def dataDecrypt(request):
    fid = request.GET.get('fileId')
    fileData = UserFilesModel.objects.get(id=fid)
    fileKey = fileData.enckey
    filename = fileData.filename

    with open(fileKey, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    loc = settings.MEDIA_ROOT + '\\' + 'files'
    file = os.path.join(loc, filename)

    with open(file, 'rb') as enc_file:
        encrypted = enc_file.read()
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    import csv
    decFile = 'decryptedFile.csv'
    with open(decFile,'wb') as f:
        f.write(decrypted)

    with open(decFile) as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename='+filename
        return response

def AdminDeactivateUsers(request):
    try:
        uid = request.GET.get('uid')
        user = UserRegistrationModel.objects.get(id=uid)
        user.status = 'deactivated'
        user.save()
        messages.success(request, f'User {user.loginid} has been deactivated successfully')
    except Exception as e:
        messages.error(request, f'Error deactivating user: {str(e)}')
    return ViewRegisteredUsers(request)