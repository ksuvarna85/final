from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    return render(request,'design_home.html')

def ngo_signup(request):
    error=""
    if request.method=='POST':
        ngo_name=request.POST.get('ngo_name')
        emailid=request.POST.get('emailid')
        password=request.POST.get('password')
        contact=request.POST.get('contact')
        certificate=request.FILES.get('certificate')
        image=request.FILES.get('image')
        description=request.POST.get('description')
        registration_number=request.POST.get('registration_number')
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        address_line_1=request.POST.get('address_line_1')


        try:
            user= User.objects.create_user(
                username=emailid,
                password=password,
                is_active=True,
            )
            user.save()
            user_additional_data=NGOProfile.objects.create(
                user=user,
                contact=contact,
                certificate=certificate,
                country=country,
                state=state,
                city=city,
                pincode=pincode,
                address_line_1=address_line_1,
                registration_number=registration_number,
                ngo_name=ngo_name,
                image=image,
                description=description,
            )
            user_additional_data.save()

            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'ngo_signup.html',d)


def user_signup(request):
    error=""
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        emailid=request.POST.get('emailid')
        password=request.POST.get('password')
        contact=request.POST.get('contact')
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        address_line_1=request.POST.get('address_line_1')


        try:
            user= User.objects.create_user(
                username=emailid,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_active=True,
            )
            user.save()
            user_additional_data=UserProfile.objects.create(
                user=user,
                contact=contact,
                country=country,
                state=state,
                city=city,
                pincode=pincode,
                address_line_1=address_line_1,
            )
            user_additional_data.save()


            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'user_signup.html',d)

def ngo_login(request):
    error=""
    if request.method == 'POST':
        email_id= request.POST['emailid']
        pass_word= request.POST['pwd']
        user = authenticate(username=email_id,password=pass_word)
        user_exists=NGOProfile.objects.filter(user=user.id).exists()
        try:
            if user and user_exists:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error = "yes"
    d= {'error':error}
    return render(request,'ngo_login.html',d)

def user_login(request):
    error=""
    if request.method == 'POST':
        email_id= request.POST['emailid']
        pass_word= request.POST['pwd']
        user = authenticate(username=email_id,password=pass_word)
        user_exists=UserProfile.objects.filter(user=user.id).exists()
        try:
            if user and user_exists:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error = "yes"
    d= {'error':error}
    return render(request,'user_login.html',d)

def adminlogin(request):
    error=""
    if request.method == 'POST':
        user_name= request.POST['uname']
        pass_word= request.POST['pwd']
        user = authenticate(username=user_name,password=pass_word)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error = "yes"
    d= {'error':error}
    return render(request,'adminlogin.html',d)

def adminhome(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    return render(request,'adminhome.html')

def Logout(request):
    logout(request)
    return redirect('home')

def ngo_profile(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        user = None
    try:
        data = NGOProfile.objects.get(user=user)
    except NGOProfile.DoesNotExist:
        data = None
    d={'user':user,'data':data}
    return render(request,'ngo_profile.html',d)

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        user = None
    try:
        data = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        data = None
    d={'user':user,'data':data}
    return render(request,'user_profile.html',d)

def all_verified_ngos(request):
    if not request.user.is_authenticated:
        return redirect('home')
    ngos=NGOProfile.objects.filter(verfied=True)
    d={'ngos':ngos}
    return render(request,'all_verified_ngos.html',d)

def all_nonverified_ngos(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    ngos=NGOProfile.objects.filter(verfied=False)
    d={'ngos':ngos}
    return render(request,'all_nonverified_ngos.html',d)

def verify_ngo(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
    ngo = NGOProfile.objects.get(id=pid)
    ngo.verfied=True
    ngo.save()
    return redirect('all_nonverified_ngos')

def delete_ngo(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
    ngo=NGOProfile.objects.get(id=pid)
    user=User.objects.get(id=ngo.user.id)
    user.delete()
    return redirect('all_nonverified_ngos')

def view_users(request):
    if not request.user.is_staff:
        return redirect('adminlogin')
    users = UserProfile.objects.all()
    ngos = NGOProfile.objects.all()
    d={'users':users,'ngos':ngos}
    return render(request,'view_users.html',d)

def delete_ngo_2(request,pid):
    if not request.user.is_staff:
        return redirect('adminlogin')
    ngo=NGOProfile.objects.get(id=pid)
    user=User.objects.get(id=ngo.user.id)
    user.delete()
    return redirect('view_users')

def changepassworduser(request):
    error=""
    if not request.user.is_authenticated:
        return redirect('user_login')
    if request.method=='POST':
        o=request.POST.get('old')
        n=request.POST.get('new')
        c=request.POST.get('confirm')
        if c==n:
            u=User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request,'changepassworduser.html',d)

def changepasswordngo(request):
    error=""
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    if request.method=='POST':
        o=request.POST.get('old')
        n=request.POST.get('new')
        c=request.POST.get('confirm')
        if c==n:
            u=User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request,'changepasswordngo.html',d)

def ngo_add_requirements(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    error=""
    if request.method=='POST':
        requirement=request.POST.get('requirement')
        quantity=request.POST.get('quantity')
        message=request.POST.get('message')
        n= NGOProfile.objects.get(user=request.user.id)
        print(n)
        try:
            user= NgoRequirements.objects.create(ngo=n,requirement=requirement,quantity=quantity,message=message)
            user.save()
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'ngo_add_requirements.html',d)


def user_ngo_view(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    ngos=NGOProfile.objects.filter(verfied=True)
    return render(request,'user_ngo_view.html',{"ngos":ngos})


def user_ngo_information(request,ngo_pk):
    if not request.user.is_authenticated:
        return redirect('user_login')

    ngo=NGOProfile.objects.get(id=ngo_pk)
    ngo_req=NgoRequirements.objects.filter(ngo=ngo)
    user=User.objects.get(username=ngo)
    ngo_details=NGOProfile.objects.get(user=user)
    error=""
    if request.method=="POST":
        arr=[]
        arr2=[]
        for i in ngo_req:
            arr.append(i.id)
            a=request.POST.get("donation"+str(i.id))
            if a=="":
                a=0
            else:
                a=int(a)
            if int(i.quantity)<=a:
                i.quantity=0
            else:
                i.quantity=int(i.quantity)-a
            i.save()
            arr2.append(int(a))

        for i in range(len(arr2)):
            if arr2[i]!=0:
                requirement=NgoRequirements.objects.get(id=arr[i]).requirement
                donated_items=arr2[i]
                user=User.objects.get(id=request.user.id)
                user_profile=UserProfile.objects.get(user=user)
                Reciept.objects.create(
                    ngo=ngo,
                    user=user_profile,
                    ngo_add_requirement=requirement,
                    donated_items=donated_items
                    ).save()
        error="no"


    data={"ngo_req":ngo_req,"ngo_details":ngo_details,'error':error}
    return render(request,"user_ngo_information.html",data)

def user_donator_list(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    a=User.objects.get(id=request.user.id)
    b=NGOProfile.objects.get(user=a)
    c=Reciept.objects.filter(ngo=b)
    d={'users':c}

    return render(request,'user_donator_list.html',d)

def ngo_self_requirements(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    ngo=User.objects.get(id=request.user.id)
    ngo_data=NGOProfile.objects.get(user=ngo)
    ngo_req=NgoRequirements.objects.filter(ngo=ngo_data)
    print(ngo_req)
    d={'ngo_req':ngo_req,'ngo_details':ngo_data}

    return render(request,"ngo_self_requirements.html",d)
