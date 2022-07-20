from itertools import count
from account.models import Employee
from jobapp.models import Curate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
# from django.urls import reverse, reverse_lazy

from account.forms import *
# from jobapp.permission import user_is_employee 
from django.http import JsonResponse

# Create your views here.
def employee_registration(request):
    msg = ''
    data = {}
    form = EmployeeRegistrationForm(request.POST or None)
    if request.method == "POST":
        email = request.POST.get('email')
        pas = request.POST.get('password1')
        cpas = request.POST.get('password2')
        print(email)
        if form.is_valid():
            form = form.save()
            auth.login(request, form)
            data['msg']="Succefully Sign Up";
            return JsonResponse(data)
        else:
            data['msg'] = "Email already exist !";
            return JsonResponse(data)
    context={
            'form':form
        }

    return render(request,'account/employee-registration.html',context)

def employer_registration(request):
    msg = ''
    data = {}
    form = EmployerRegistrationForm(request.POST or None)
    if request.method == "POST":
        email = request.POST.get('email')
        pas = request.POST.get('password1')
        cpas = request.POST.get('password2')
        if form.is_valid():
            form = form.save()
            auth.login(request, form)
            data['msg']="Succefully Sign Up";
            return JsonResponse(data)
        else:
            data['msg'] = "Email already exist !";
            return JsonResponse(data)
    return render(request,'account/employer-registration.html')

def user_logIn(request):
    form = UserLoginForm(request.POST or None)
    msg = ''
    data = {}
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            pas = request.POST.get('password')
            print(email, pas)
            if form.is_valid():
                auth.login(request, form.get_user())
                emp=Employer.objects.filter(user=request.user)
                if emp.count() > 0:
                    data['type']="employer"
                else:
                    data['type']="employee"
                return JsonResponse(data)
            else:
                data['msg']="Email or Password is Incorrect";
                return JsonResponse(data)
    context = {
        'form': form,
    }
    return render(request,'account/login.html',context)


def user_logOut(request):
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')