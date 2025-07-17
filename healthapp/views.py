from random import randint

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from healthapp.models import*

# Create your views here.
def index(request):
    return render(request, "index.html", locals())

def user_dashboard(request):
    data = Test.objects.all()
    d = {'data': data}
    return render(request, "user_dashboard.html", locals())

def dashboard(request):
    fullname = Member.objects.filter()
    user = Register.objects.filter()
    pressure = Pressure.objects.filter()
    sugar = Sugar.objects.filter()
    temprature = Temprature.objects.filter()
    return render(request, "dashboard.html", locals())

def user_login(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(username=email, password=pwd)
        if user:
            if user.is_staff:
                messages.success(request, "Invalid User")
                return redirect('user_login')
            else:
                login(request, user)
                messages.success(request, "User Login Successful")
                return redirect('user_dashboard')
        else:
            messages.success(request, "Invalid User")
            return redirect('user_login')
    return render(request, "user_login.html")

@login_required(login_url='/user_login/')
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('user_login')

def user_register(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        pwd = request.POST['password']

        user = User.objects.create_user(first_name=fullname, username=email, password=pwd)
        Register.objects.create(user=user, mobile=mobile)
        messages.success(request, "Register Successful")
        return redirect('user_login')
    return render(request, "user_register.html")

@login_required(login_url='/user_login/')
def user_profile(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']

        user = User.objects.filter(id=request.user.id).update(first_name=fullname, email=email)
        Register.objects.filter(user=request.user).update(mobile=mobile)
        messages.success(request, "Updation Successful")
        return redirect('user_profile')
    data = Register.objects.get(user=request.user)
    return render(request, "user_profile.html", locals())

@login_required(login_url='/admin_login/')
def view_reg_user(request):
    data = Register.objects.all()
    d = {'data': data}
    return render(request, "view_reg_user.html", locals())


def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            if user.is_staff:
                login(request, user)
                messages.success(request, "Admin Login Successful")
                return redirect('dashboard')
            else:
                messages.success(request, "Invalid Admin")
                return redirect('admin_login')
    return render(request, "admin_login.html")

@login_required(login_url='/admin_login/')
def logout_admin(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('admin_login')

@login_required(login_url='/user_login/')
def add_member(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        age = request.POST['age']
        gender = request.POST['gender']
        weight = request.POST['weight']
        relation = request.POST['relation']

        user = Register.objects.get(user=request.user)
        Member.objects.create(fullname=fullname, age=age, gender=gender, weight=weight, user=user, relation=relation)
        messages.success(request, "Add Successful")
        return redirect('add_member')
    return render(request, "add_member.html", locals())

@login_required(login_url='/admin_login/')
def add_testing_range(request):
    if request.method == "POST":
        testname = request.POST['testname']

        Test.objects.create(testname=testname,)
        messages.success(request, "Add Successful")
        return redirect('add_testing_range')
    return render(request, "add_testing_range.html", locals())

@login_required(login_url='/user_login/')
def add_blood_pressure(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        sysmmhg = request.POST['sysmmhg']
        diammhg = request.POST['diammhg']
        pluses = request.POST['pluses']
        memberobj = Member.objects.get(id=fullname)

        user = Register.objects.get(user=request.user)
        Pressure.objects.create(fullname=memberobj, sysmmhg=sysmmhg, user=user, diammhg=diammhg, pluses=pluses)
        messages.success(request, "Add Successful")
        return redirect('add_blood_pressure')
    mymember = Member.objects.all()
    return render(request, "add_blood_pressure.html", locals())

@login_required(login_url='/user_login/')
def add_blood_sugar(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        typesofbloodsugar = request.POST['typesofbloodsugar']
        bloodsugarmgdl = request.POST['bloodsugarmgdl']
        memberobj = Member.objects.get(id=fullname)

        Sugar.objects.create(fullname=memberobj, typesofbloodsugar=typesofbloodsugar, bloodsugarmgdl=bloodsugarmgdl)
        messages.success(request, "Add Successful")
        return redirect('add_blood_sugar')
    mymember = Member.objects.all()
    return render(request, "add_blood_sugar.html", locals())

@login_required(login_url='/user_login/')
def add_body_temprature(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        bodytemprature = request.POST['bodytemprature']
        memberobj = Member.objects.get(id=fullname)

        Temprature.objects.create(fullname=memberobj, bodytemprature=bodytemprature)
        messages.success(request, "Add Successful")
        return redirect('add_body_temprature')
    mymember = Member.objects.all()
    return render(request, "add_body_temprature.html", locals())

@login_required(login_url='/user_login/')
def manage_blood_pressure(request):
    user = Register.objects.get(user=request.user)
    data = Pressure.objects.filter(user=user)
    d = {'data': data}
    return render(request, "manage_blood_pressure.html", locals())

@login_required(login_url='/user_login/')
def manage_blood_sugar(request):
    data = Sugar.objects.all()
    d = {'data': data}
    return render(request, "manage_blood_sugar.html", locals())

@login_required(login_url='/user_login/')
def manage_body_temprature(request):
    data = Temprature.objects.all()
    d = {'data': data}
    return render(request, "manage_body_temprature.html", locals())

def history_blood_pressure(request, pid):
    data=Pressure.objects.get(id=pid)
    return render(request,'history_blood_pressure.html',locals())

def history_blood_sugar(request, pid):
    data=Sugar.objects.get(id=pid)
    return render(request,'history_blood_sugar.html',locals())

def history_body_temprature(request, pid):
    data=Temprature.objects.get(id=pid)
    return render(request,'history_body_temprature.html',locals())

@login_required(login_url='/user_login/')
def manage_member(request):
    user = Register.objects.get(user=request.user)
    data = Member.objects.filter(user=user)
    d = {'data': data}
    return render(request, "manage_member.html", locals())

@login_required(login_url='/user_login/')
def edit_member(request, pid):
    if request.method == "POST":
        fullname = request.POST['fullname']
        age = request.POST['age']
        gender = request.POST['gender']
        weight = request.POST['weight']
        relation = request.POST['relation']

        Member.objects.filter(id=pid).update(fullname=fullname, age=age, gender=gender, weight=weight, relation=relation)
        messages.success(request, "Updated Successful")
        return redirect('manage_member')
    data = Member.objects.get(id=pid)
    return render(request, "edit_member.html", locals())

@login_required(login_url='/user_login/')
def delete_member(request, pid):
    data = Member.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect("manage_member")

@login_required(login_url='/admin_login/')
def delete_testing_range(request, pid):
    data = Test.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect("manage_testing_range")

@login_required(login_url='/user_login/')
def delete_blood_pressure(request, pid):
    data = Pressure.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect("manage_blood_pressure")

@login_required(login_url='/user_login/')
def delete_blood_sugar(request, pid):
    data = Sugar.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect("manage_blood_sugar")

@login_required(login_url='/user_login/')
def delete_body_temprature(request, pid):
    data = Temprature.objects.get(id=pid)
    data.delete()
    messages.success(request, "Delete Successful")
    return redirect("manage_body_temprature")

@login_required(login_url='/admin_login/')
def update_testing_range(request, pid):
    if request.method == "POST":
        testname = request.POST['testname']
        description = request.POST['editor1']

        Test.objects.filter(id=pid).update(testname=testname, description=description)
        messages.success(request, "Updated Successful")
        return redirect('manage_testing_range')
    data = Test.objects.get(id=pid)
    return render(request, "update_testing_range.html", locals())

@login_required(login_url='/admin_login/')
def manage_testing_range(request):
    data = Test.objects.all()
    d = {'data': data}
    return render(request, "manage_testing_range.html", locals())

@login_required(login_url='/admin_login/')
def change_password(request):
    # user = User.objects.get(username=request.user.username)
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('change_password')

    return render(request,'change_password.html')

@login_required(login_url='/user_login/')
def user_change_password(request):
    # user = User.objects.get(username=request.user.username)
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            messages.success(request, "Password changed successfully")
            return redirect('/')
        else:
            messages.success(request, "New password and confirm password are not same.")
            return redirect('user_change_password')
    return render(request,'user_change_password.html')

@login_required(login_url='/user_login/')
def blood_pressure_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        fullname = request.POST['fullname']

        data = Pressure.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate, fullname__id=fullname)
        data2 = True
    fullname = Member.objects.all()
    return render(request, "blood_pressure_report.html", locals())

@login_required(login_url='/admin_login/')
def admin_bp_report(request):
    userid = request.GET.get('user', None)
    fullname = None
    user = None
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        fullname = request.POST['fullname']

        data = Pressure.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate, fullname__id=fullname,)
        data2 = True
    user = Register.objects.all()
    return render(request, "admin_bp_report.html", locals())

def fullname(request):
    userid = request.GET.get('user', None)
    fullname = Member.objects.filter(user__id=userid)
    return render(request, 'fullname.html', locals())

@login_required(login_url='/user_login/')
def blood_sugar_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        fullname = request.POST['fullname']

        data = Sugar.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate, fullname__id=fullname)
        data2 = True
    fullname = Member.objects.all()
    return render(request, "blood_sugar_report.html", locals())

@login_required(login_url='/admin_login/')
def admin_bs_report(request):
    userid = request.GET.get('user', None)
    fullname = None
    user = None
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        fullname = request.POST['fullname']

        data = Sugar.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate, fullname__id=fullname)
        data2 = True
    user = Register.objects.all()
    mem = Member.objects.filter()
    return render(request, "admin_bs_report.html", locals())

@login_required(login_url='/user_login/')
def body_temprature_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        fullname = request.POST['fullname']

        data = Temprature.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate, fullname__id=fullname)
        data2 = True
    fullname = Member.objects.all()
    return render(request, "body_temprature_report.html", locals())

@login_required(login_url='/admin_login/')
def admin_bt_report(request):
    data = None
    data2 = None
    if request.method == "POST":
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        fullname = request.POST['fullname']

        data = Temprature.objects.filter(creationdate__gte=fromdate, creationdate__lte=todate, fullname=fullname)
        data2 = True
    user = Register.objects.all()
    mem = Member.objects.filter()
    return render(request, "admin_bt_report.html", locals())




