from django.shortcuts import render
from django.http import JsonResponse
from django.urls import is_valid_path, reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from . import models
from .forms import *
from .models import Resume, Skill as AccSkill
from jobapp.permissions import *
from jobapp.models import *


# Create your views here.
@login_required(login_url=reverse_lazy('account:login'))
def employee_profile(request):
    if request.method == "POST":
        
        pro = EmployeeProfile.objects.get(user=request.user.employee)
        id = pro.id
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        mob = request.POST.get('mobile')
        about = request.POST.get('bio')
        
        loc = request.POST.get('location')
        account = request.POST.get('account_type')
        poe = request.POST.get('passing_out_year')
        exp = request.POST.get('years_of_experience')
        np = request.POST.get('notice_period')
        snp = request.POST.get('s_notice_period')
        
        
        # EmployeeProfileEditForm(first_name=fname, last_name=lname).save()
        form1 = EmployeeProfileEditForm(request.POST, instance=request.user)
        form2 = EmployeeProfile2EditForm(request.POST, instance=request.user)
        if (form1.is_valid()):
            form1.save()

            EmployeeProfile(id=id, user=request.user.employee, bio=about, location=loc, account_type=account, passing_out_year=poe, years_of_experience=exp, notice_period=np, s_notice_period=snp).save()
            # print(id, fname, lname, account, about, exp, loc, mob, poe)
            # print("Hello")
        # print(id, fname, lname, account, about, exp, loc, mob, poe)
        data = {}
        data["first_name"]=fname
        data["last_name"]=lname
        data["account_type"] = account
        return JsonResponse(data)
    profile = EmployeeProfile.objects.get(user = request.user.id)
    skills = AccSkill.objects.filter(user = request.user.id)
    work = WorkExperience.objects.filter(user = request.user.id).order_by('-year_of_join')
    lng = SpokenLanguage.objects.filter(user = request.user.id)
    cert = Certificate.objects.filter(user = request.user.id)
    edu = Education.objects.filter(user = request.user.id).order_by('-year_of_join')
    resume = Resume.objects.filter(user = request.user.id)
    
    
    eduForm = EducationAddForm()
    expForm = ExperienceAddForm()
    cerForm = CertificateAddForm()
    sklForm = SkillsAddForm()
    lngForm = LanguageAddForm()
    context = {'profile': profile, 'skills': skills, 'lng': lng, 'work': work, 
                'cert': cert, 'eduForm': eduForm, 'expForm': expForm, 'cerForm': cerForm,
                'sklForm':sklForm, 'lngForm': lngForm, 'edu': edu, 'resume': resume}
    return render(request, 'employee/employee-profile.html', context)
    # return render(request, 'jobapp/employee-profile.html')


def exp_save(request):
    if request.method == "POST":
        form = ExperienceAddForm(request.POST)
        expid = request.POST.get('expid')
        exptitle = request.POST['expTitle']
        expcompany = request.POST['expCompany']
        expsyear = request.POST['expsyear']
        expeyear = request.POST['expeyear']
        expbody = request.POST['expbody']
        if (expid == ""):
            exp = WorkExperience(user=request.user.employee, title=exptitle, company=expcompany, year_of_join=expsyear, year_of_end=expeyear, expbody=expbody)
        else:
            exp = WorkExperience(id=expid, user=request.user.employee, title=exptitle, company=expcompany, year_of_join=expsyear, year_of_end=expeyear, expbody=expbody)
        
        exp.save()
        expdata = WorkExperience.objects.filter(user=request.user.employee).order_by('year_of_join').values()
        # print(expdata)
        exp_data = list(expdata)
        return JsonResponse({'status': "Save", "exp_data": exp_data})
    else:
        return JsonResponse({'status': '0'})


def edu_save(request):
    if request.method == "POST":
        form = ExperienceAddForm(request.POST)
        
        eduid = request.POST.get('eduid')
        edutitle = request.POST['edutitle']
        educollege = request.POST['educollege']
        edusyear = request.POST['edusyear']
        edueyear = request.POST['edueyear']
        edubody = request.POST['edubody']
        if(eduid == ""):
            edu = Education(user=request.user.employee, title=edutitle, college=educollege, year_of_join=edusyear, year_of_end=edueyear, edubody=edubody)
        else:
            edu = Education(id= eduid, user=request.user.employee, title=edutitle, college=educollege, year_of_join=edusyear, year_of_end=edueyear, edubody=edubody)
        edu.save()
        yearf = int(edusyear)
        edudata = Education.objects.filter(user=request.user.employee).order_by('year_of_join').values()
        # print(edudata)
        edu_data = list(edudata)
        return JsonResponse({'status': "Save", "edu_data": edu_data})
    else:
        return JsonResponse({'status': '0'})

def cer_save(request):
    if request.method == "POST":
        form = ExperienceAddForm(request.POST)
        cerid = request.POST.get('cerid')
        certitle = request.POST['certitle']
        cercompany = request.POST['cercompany']
        cerurl = request.POST['cerurl']
        if (cerid == ""):
            cer = Certificate(user=request.user.employee, title=certitle, company=cercompany, url=cerurl)
        else:
            cer = Certificate(id=cerid, user=request.user.employee, title=certitle, company=cercompany, url=cerurl)
        cer.save()
        cerdata = Certificate.objects.filter(user=request.user.employee).values()
        # print(cerdata)
        cer_data = list(cerdata)
        return JsonResponse({'status': "Save", "cer_data": cer_data})
    else:
        return JsonResponse({'status': '0'})

def skl_save(request):
    if request.method == "POST":
        form = ExperienceAddForm(request.POST)
        
        skltitle = request.POST['skltitle']
        sklexperties = request.POST['sklexperties']
        sklset = request.POST['sklset']
        skl = AccSkill(user=request.user.employee, title=skltitle, experties=sklexperties, skill_set=sklset)
        skl.save()
        skldata = AccSkill.objects.filter(user=request.user.employee).values()
        # print(skldata)
        skl_data = list(skldata)
        return JsonResponse({'status': "Save", "skl_data": skl_data})
    else:
        return JsonResponse({'status': '0'})

def lng_save(request):
    if request.method == "POST":
        form = ExperienceAddForm(request.POST)
        
        lngtitle = request.POST['lngtitle']
        lngexperties = request.POST['lngexperties']
        lng = SpokenLanguage(user=request.user.employee, title=lngtitle, experties=lngexperties)
        lng.save()
        lngdata = SpokenLanguage.objects.filter(user=request.user.employee).values()
        # print(lngdata)
        lng_data = list(lngdata)
        return JsonResponse({'status': "Save", "lng_data": lng_data})
    else:
        return JsonResponse({'status': '0'})

def edu_delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = Education.objects.get(pk=id)
        pi.delete()
        edudata = Education.objects.filter(user=request.user.employee).order_by('year_of_join').values()
        edu_data = list(edudata)
        return JsonResponse({ "status": 1, "edu_data": edu_data})
    else:
        return JsonResponse({ "status": 0})

def exp_delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = WorkExperience.objects.get(pk=id)
        pi.delete()
        expdata = WorkExperience.objects.filter(user=request.user.employee).order_by('year_of_join').values()
        exp_data = list(expdata)
        return JsonResponse({ "status": 1, 'exp_data': exp_data})
    else:
        return JsonResponse({ "status": 0})

def cer_delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = Certificate.objects.get(pk=id)
        pi.delete()
        cerdata = Certificate.objects.filter(user=request.user.employee).values()
        cer_data = list(cerdata)
        return JsonResponse({ "status": 1, 'cer_data': cer_data})
    else:
        return JsonResponse({ "status": 0})

def skl_delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = AccSkill.objects.get(pk=id)
        pi.delete()
        return JsonResponse({ "status": 1})
    else:
        return JsonResponse({ "status": 0})

def lng_delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = SpokenLanguage.objects.get(pk=id)
        pi.delete()
        return JsonResponse({ "status": 1})
    else:
        return JsonResponse({ "status": 0})

def edu_edit(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = Education.objects.get(pk=id)
        pi_data = {"id":pi.id, "title":pi.title,"college": pi.college, "year_of_join": pi.year_of_join, "year_of_end": pi.year_of_end, "edubody": pi.edubody}
        return JsonResponse(pi_data)

def exp_edit(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = WorkExperience.objects.get(pk=id)
        pi_data = {"id":pi.id, "title":pi.title,"company": pi.company, "year_of_join": pi.year_of_join, "year_of_end": pi.year_of_end, "expbody": pi.expbody}
        return JsonResponse(pi_data)

def cer_edit(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = Certificate.objects.get(pk=id)
        pi_data = {"id":pi.id, "title":pi.title,"company": pi.company, "url": pi.url}
        return JsonResponse(pi_data)


@login_required(login_url=reverse_lazy('account:login'))
def employee_dashboard(request):
    savedjobs = []
    appliedjobs = []
    profile = EmployeeProfile.objects.get(user=request.user.employee)
    savedjobs = BookmarkJob.objects.filter(user=request.user.id)
    appliedjobs = Applicant.objects.filter(user=request.user.id)
    job = Job.objects.filter(status="Active").order_by('-timestamp')
    

    context = {
        'savedjobs': savedjobs,
        'appliedjobs':appliedjobs,
        'length': len(appliedjobs),
        'related_job_list': job,
        'profile': profile,
    }
    return render(request, 'employee/employee-dashboard.html', context)

def resume_create(request):
    if request.method == "POST" and 'resumeimage' in request.FILES:
        title = request.POST.get('resumeTitle')
        image = request.FILES.get('resumeimage')
        print("HERE")
        print(str(image), title, request.user)
        
        res = Resume(user=request.user.employee, title=title, file=image)
        res.save()
        print("YESS")
        return JsonResponse({'status': 1})
    else:
        print("NO")
        return JsonResponse({'status': 0})
