from ast import IfExp
from cmath import e
from django.shortcuts import render
from django.template import context
from .models import *
from django.http import JsonResponse
from jobapp.permissions import *
from .forms import GalleryImageUpload
from cProfile import Profile
from re import search
import re
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import is_valid_path, reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from datetime import datetime, timedelta
from django.utils import timezone
import datetime
# from account.models import Education, User, EmployeeProfile, SpokenLanguage, WorkExperience, Certificate
from account.models import User
# from jobapp.forms import *
from jobapp.models import *
from jobapp.models import Skill as sk
from employee.models import *
from employer.models import *
# from jobapp.permission import *
# from account.models import Skill as AccSkill
User = get_user_model()

# Create your views here.

def job_bookmark(request):
    savedjobs = BookmarkJob.objects.filter(user=request.user.id)
    return render(request, 'employee/bookmark-jobs.html',
    {
        'bookmark': savedjobs
    })

def bookmark_delete(request):
    arr = []
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = BookmarkJob.objects.get(pk=id)
        pi.delete()
        bookmark = BookmarkJob.objects.filter(user=request.user.employee)
        
        for b in bookmark:
            # print(b.job_id)
            arr.extend(Job.objects.filter(pk=b.job_id).values())

        bookmark = BookmarkJob.objects.filter(user=request.user.employee).values()
        # book_mark = list(bookmark)
        # print(bookmark)
        
        print(arr)
        return JsonResponse({ "status": 1, "book_mark": list(bookmark), 'arr':arr})
    else:
        return JsonResponse({ "status": 0})


def job_applied(request):
    appliedjobs = Applicant.objects.filter(user=request.user.id)
    return render(request, 'employee/applied-jobs.html',
    {
        'apply': appliedjobs
    })

def applied_delete(request):
    arr = []
    if request.method == "POST":
        id = request.POST.get('sid')
        # print(id)
        pi = Applicant.objects.get(pk=id)
        pi.delete()
        appliedjob = Applicant.objects.filter(user=request.user)
        
        for b in appliedjob:
            # print(b.job_id)
            arr.extend(Job.objects.filter(pk=b.job_id).values())
        appliedjob = Applicant.objects.filter(user=request.user).values()
        applied_job = list(appliedjob)
        return JsonResponse({ "status": 1, "applied_job": applied_job, 'arr': arr})
    else:
        return JsonResponse({ "status": 0})






def job_list_View(request):
    job_list = Job.objects.filter(status=2).order_by('-timestamp')

    if request.method == "POST":
        if 'curateDataEnter' in request.POST:
            job_listCD = Job.objects.filter(status=2).order_by('-timestamp')
            job_listCD2 = Job.objects.filter(status=2).order_by('-timestamp')
            arrCD=[]
            arrCD2=[]
            arrCD3=[]
            cur = Curate.objects.filter(user = request.user.employee)
            levelD = request.POST['level']
            job_typeD = request.POST['job_type']
            roleD = request.POST['role']
            locationD = request.POST['location']
            skillD = request.POST['skill']
            workplaceD = request.POST['workplace']
            nameD = request.POST['name']
            if not cur.exists():
                isDD=True
            else:
                if request.POST['isDefault'] == "false":
                    isDD=False
                if request.POST['isDefault'] == "true":
                    isDD=True
            
            if isDD:
                Curate.objects.filter(user=request.user.employee,is_default=True).update(is_default=False)
            if request.POST['newsLetter'] == "false":
                neLD=False
            if request.POST['newsLetter'] == "true":
                neLD=True
            curD = Curate(user=request.user.employee, level=levelD,job_type=job_typeD,role=roleD,location=locationD,skill=skillD,workplace=workplaceD,name=nameD,is_default=isDD,news_letter=neLD)
            curD.save()
            cur = Curate.objects.filter(user = request.user.employee).values()
            return JsonResponse({"S": 1,"curate" : list(cur)})
        else:
            job_list2 = Job.objects.filter(status=2).order_by('-timestamp').values()
            job_listSkill = Job.objects.filter(status=2).order_by('-timestamp')
            arr2 = []
            arrAll = []
            zLoc=0
            zSkill=0
            zRole=0
            zWork=0
            zEmp=0
            zDte=0
            if 'location2' in request.POST:
                location=request.POST.get('location2')
                if location!="0":
                    zLoc=0
                    location = location.split(",")
                    for s in location:
                        arrAll.extend(job_listSkill.filter(location__icontains=s))
                else:
                    zLoc=1
            if 'skill' in request.POST:
                skill=request.POST.get('skill')
                if skill!="0":
                    zSkill=0
                    skill = skill.split(",")
                    for s in skill:
                        arrAll.extend(job_listSkill.filter(tags__icontains=s))
                else:
                    zSkill=1
            if 'cat' in request.POST:
                cat=request.POST.get('cat')
                if cat!="0":
                    zRole=0
                    cat = cat.split(",")
                    for s in cat:
                        category2 = Role.objects.get(name=s)
                        arrAll.extend(job_listSkill.filter(role=category2.id))
                else:
                    zRole=1
            if 'workexp' in request.POST:
                workexp=request.POST.get('workexp')
                if workexp!="0":
                    zWork=0
                    workexp = workexp.split(",")
                    for w in workexp:
                        if w == "-1":
                            arrAll.extend(job_listSkill.filter(experince=""))
                        else:
                            arrAll.extend(job_listSkill.filter(experince=w))
                else:
                    zWork=1
            if 'emptype' in request.POST:
                emptype=request.POST.get('emptype')
                if emptype!="0":
                    zEmp=0
                    emptype = emptype.split(",")
                    for w in emptype:
                        arrAll.extend(job_listSkill.filter(job_type=w))
                else:
                    zEmp=1
            if 'datepost' in request.POST:
                datepost=request.POST.get('datepost')
                if datepost!="0":
                    zDte=0
                    if datepost=="-1":zDte=1
                    if datepost=="1":
                        hour_ago = datetime.now(tz=timezone.utc) - timedelta(hours = 1)
                        now = datetime.now(tz=timezone.utc)
                        arrAll.extend(job_listSkill.filter(timestamp__gte=hour_ago,timestamp__lte=now))
                    if datepost=="2":
                        hour_ago = datetime.now(tz=timezone.utc) - timedelta(hours = 24)
                        now = datetime.now(tz=timezone.utc)
                        arrAll.extend(job_listSkill.filter(timestamp__gte=hour_ago,timestamp__lte=now))
                    if datepost=="3":
                        hour_ago = datetime.now(tz=timezone.utc) - timedelta(hours = 168)
                        now = datetime.now(tz=timezone.utc)
                        arrAll.extend(job_listSkill.filter(timestamp__gte=hour_ago,timestamp__lte=now))
                    if datepost=="4":
                        hour_ago = datetime.now(tz=timezone.utc) - timedelta(hours = 336)
                        now = datetime.now(tz=timezone.utc)
                        arrAll.extend(job_listSkill.filter(timestamp__gte=hour_ago,timestamp__lte=now))
                    if datepost=="5":
                        hour_ago = datetime.now(tz=timezone.utc) - timedelta(hours = 720)
                        now = datetime.now(tz=timezone.utc)
                        arrAll.extend(job_listSkill.filter(timestamp__gte=hour_ago,timestamp__lte=now))
                else:
                    zDte=1
            if zRole==0 or zSkill==0 or zLoc==0 or zWork==0 or zEmp==0 or zDte==0:
                t=set(arrAll)
                arrr=list(t)
                for i in arrr:
                    arr2.extend(job_listSkill.filter(id=i.id).values())
                job_list2=arr2
            return JsonResponse({"data2": list(job_list2)})

    showCurate = 0
    curData = 0
    if request.user.is_authenticated:
        showCurate = 1
        cur = Curate.objects.filter(user = request.user.employee).values()
        if cur.count() == 0:
            showCurate = 1
        else:
            showCurate = 0
            curData=cur
    else:
        showCurate = -1
    data=serialize('json', job_list)    
    # curateData = Cur.objects.all().values()
    location = Location.objects.all().values()
    role = Role.objects.all().values()
    skill = Skill.objects.all().values()
    workplace = Workplace.objects.all().values()
    
    context = {
        'userCurate': curData,
        # 'curateData': curateData,
        'showCurate': showCurate,
        'role': role,
        'location': location,
        'skill': skill,
        'workplace': workplace,
        "data": data,
    }
    return render(request, 'jobapp/job-list.html', context)

def cur_delete(request):
    if request.method == "POST":
        id = request.POST.get('cdid')
        # print(id)
        pi = Curate.objects.get(pk=id)
        pi.delete()
        return JsonResponse({ "status": 1})
    else:
        return JsonResponse({ "status": 0})

def cur_view(request):
    if request.method == "POST":
        id = request.POST.get('cvid')
        # print(id)
        cur = Curate.objects.filter(user = request.user.employee).values()
        return JsonResponse({'status': 1,"curate" : list(cur)})
    else:
        return JsonResponse({ "status": 0})

def cur_edit(request):
    if request.method == "POST":
        id = request.POST.get('ceid')
        levelCU = request.POST.get('levelCU')
        job_typeCU = request.POST.get('job_typeCU')
        nameCU = request.POST.get('nameCU')
        isDefaultCUU = True if request.POST.get('isDefaultCU') == 'true' else False
        newsLetterCUU = True if request.POST.get('newsLetterCU') == 'true' else False
        roleCU = request.POST.get('roleCU')
        skillCU = request.POST.get('skillCU')
        workCU = request.POST.get('workCU')
        locCU = request.POST.get('locCU')
        if isDefaultCUU:
            Curate.objects.filter(user=request.user.employee,is_default=True).update(is_default=False)
        
        cur_obj=Curate.objects.get(pk=id)
        cur_obj.name=nameCU
        cur_obj.level=levelCU
        cur_obj.job_type=job_typeCU
        cur_obj.role=roleCU
        cur_obj.location=locCU
        cur_obj.skill=skillCU
        cur_obj.workplace=workCU
        cur_obj.is_default=isDefaultCUU
        cur_obj.news_letter=newsLetterCUU
        cur_obj.save()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})

@login_required(login_url=reverse_lazy('account:login'))
def can_aply(request):
    pass
    # if request.method == "POST":
    #     id = request.POST.get('id')
    #     applicant = Applicant.objects.filter(user = request.user,job=id).values()
    #     # print(applicant)
    #     if applicant.count() == 0:
    #         jobI = Job.objects.get(pk=id)
    #         app = Applicant(user=request.user, job=jobI)
    #         app.save()
    #         return JsonResponse({ "status": 1})
    #     else:
    #         return JsonResponse({ "status": 0})

def home_view(request):
    # pass
    
    # published_jobs = Job.objects.filter(status='2').order_by('-timestamp')
    # jobs = published_jobs.filter(status='2')
    # total_candidates = User.objects.filter(role='employee').count()
    # total_companies = User.objects.filter(role='employer').count()
    # paginator = Paginator(jobs, 3)
    # page_number = request.GET.get('page',None)
    # page_obj = paginator.get_page(page_number)

    # if request.is_ajax():
    #     job_lists=[]
    #     job_objects_list = page_obj.object_list.values()
    #     for job_list in job_objects_list:
    #         job_lists.append(job_list)
        

    #     next_page_number = None
    #     if page_obj.has_next():
    #         next_page_number = page_obj.next_page_number()

    #     prev_page_number = None       
    #     if page_obj.has_previous():
    #         prev_page_number = page_obj.previous_page_number()

    #     data={
    #         'job_lists':job_lists,
    #         'current_page_no':page_obj.number,
    #         'next_page_number':next_page_number,
    #         'no_of_page':paginator.num_pages,
    #         'prev_page_number':prev_page_number
    #     }    
    #     return JsonResponse(data)
    
    # context = {

    # 'total_candidates': total_candidates,
    # 'total_companies': total_companies,
    # 'total_jobs': len(jobs),
    # 'total_completed_jobs':len(published_jobs.filter(is_closed=True)),
    # 'page_obj': page_obj
    # }
    # # print('ok')
    return render(request, 'jobapp/index.html')

def about(request):
    return render(request, 'jobapp/about.html')

def contact(request):
    return render(request, 'jobapp/contact.html')

def single_job_view(request, id):
    """
    Provide the ability to view job details
    """
    data = Job.objects.filter(status = 2)[:3]
    # user = get_object_or_404(Employee, id=request.user.employee)
    user = request.user.employee
    print(user)
    job2=Job.objects.filter(id=id)
    job3=Job.objects.get(id=id)
    user = job3.user.employer
    emp = EmployerProfile.objects.get(user=user)
    print(emp.id)
    lang = Language.objects.filter(user=job3.user_id).filter(job__in=job2).values()
    # print(data)
    try:
        print("here-1")
        job = get_object_or_404(Job, id=id)
        # related_job_list = job.tags.similar_objects()
        # user = get_object_or_404(User, id=request.user.employee)
        user = request.user.employee
        print(user)
        tag = job.tags.split(',')
        apply_exist = Applicant.objects.filter(user=user, job=job).exists()
        book_exist = BookmarkJob.objects.filter(user=user, job=job).exists()
        
        
        if request.method == "POST":
            # print(request.POST.get("form_type"))
            
            if request.POST.get("form_type") == 'form1app':
                if request.user.employee:
                    
                    if not apply_exist:
                        applicant = Applicant.objects.create(user=user, job=job, status = '1')
                        applicant.save()
                        print("Done here")
                        return redirect('jobapp:job_applied')
                    return redirect('jobapp:job_applied')
        
            elif request.POST.get("form_type") == 'form2book':
                if request.user.employee:
                    
                    if not book_exist:
                        book = BookmarkJob.objects.create(user=user, job=job)
                        book.save()
                        print("Done here Book")
                        return redirect('jobapp:job_bookmark')  
                    return redirect('jobapp:job_bookmark')
        context = {
            'job': job,
            'tag':tag,
            'apply_exist': apply_exist,
            'book_exist': book_exist,
            'data': data,
            'total_lang':lang,
            'emp': emp
        }
        return render(request, 'jobapp/job-details.html', context)
    except:
        print("here-2")
        job = get_object_or_404(Job, id=id)
        tag = job.tags.split(',')
        return render(request, 'jobapp/job-details.html',{
            'job':job,
            'tag': tag,
            'data': data,
            'total_lang':lang,
            'emp': emp,
        })

def naman(request, id):
    applicant = Applicant.objects.get(id=id)
    job = applicant.job
    if request.method == "POST":
        title = request.POST.get('title')
        round_no = request.POST.get('round_no')
        interview_date = request.POST.get('interview_date')
        interview_start_time = request.POST.get('interview_start_time')
        interview_end_time = request.POST.get('interview_end_time')
        name = request.POST.get('name')
        if name == "passFORM":
            intid = request.POST.get('id')
            print(intid)
            Interview.objects.filter(id=intid).update(second_status='1')
            all_int = Interview.objects.filter(user=applicant.user, job=job).order_by('-round_no').reverse()
            context = {

                'applicant': applicant,
                'all_int': all_int

            }
            return render(request, 'ats/naman.html', context)
        elif name == 'rejectFORM':
            intid = request.POST.get('id')
            print(intid)
            Interview.objects.filter(id=intid).update(second_status='2')
            all_int = Interview.objects.filter(user=applicant.user, job=job).order_by('-round_no').reverse()
            context = {

                'applicant': applicant,
                'all_int': all_int

            }
            return render(request, 'ats/naman.html', context)
        elif name == 'holdFORM':
            intid = request.POST.get('id')
            print(intid)
            Interview.objects.filter(id=intid).update(second_status='3')
            all_int = Interview.objects.filter(user=applicant.user, job=job).order_by('-round_no').reverse()
            context = {

                'applicant': applicant,
                'all_int': all_int

            }
            return render(request, 'ats/naman.html', context)
        try:
            inter = Interview.objects.create(user=applicant.user, job=job, title=title, round_no=round_no,
                    interview_date=interview_date, interview_start_time=interview_start_time,
                    interview_end_time=interview_end_time, status='3'
            )
            print(inter.id)
            return JsonResponse({'status': 1, 'id': (inter.id)})
        except:
            return JsonResponse({'status': 0})
        

    all_int = Interview.objects.filter(user=applicant.user, job=job).order_by('-round_no').reverse()
    # print(all_int)
    context = {

        'applicant': applicant,
        'all_int': all_int

    }
    return render(request, 'ats/naman.html', context)


def naman3(request, id):
    all_applicants = Applicant.objects.filter(job=id)

    context = {

        'all_applicants': all_applicants
    }
    return render(request, 'ats/naman3.html', context)

@user_is_employer
def total_job_view(request):
    jobs = []
    total_applicants = {}
    if request.user.employer:

        jobs = Job.objects.filter(user=request.user.id, status='2')
        
        for job in jobs:
            count = Applicant.objects.filter(job=job.id).count()
            total_applicants[job.id] = count

    if request.method == "POST":
        t_app = {}
        if request.POST.get('deptData'):
            deptid=request.POST.get('deptData')
            job_obj=Job.objects.filter(dept=deptid).filter(user=request.user.id, status='2').values()            
            job_obj2=Job.objects.filter(dept=deptid).filter(user=request.user.id, status='2')
            for job in job_obj2:
                count = Applicant.objects.filter(job=job.id).count()
                t_app[job.id] = count
            print(t_app)
            return JsonResponse({'status': 1,'data2': list(job_obj),'total_applicant':t_app})
        else:
            job_obj=Job.objects.filter(user=request.user.id, status='2').values()
            job_obj2=Job.objects.filter(user=request.user.id, status='2')
            for job in job_obj2:
                count = Applicant.objects.filter(job=job.id).count()
                t_app[job.id] = count
            print(t_app)
            return JsonResponse({'status': 1,'data2': list(job_obj),'total_applicant':t_app})

        
    total_dept = Department.objects.filter(user=request.user.employer).values()
    context = {
        'total_dept':total_dept,
        'jobs': jobs,
        'total_applicants': total_applicants,
    }
    return render(request, 'ats/naman2.html', context)

@user_is_employer
def archivied_job_view(request):
    jobs = []
    total_applicants = {}
    if request.user.employer:

        jobs = Job.objects.filter(user=request.user.id, status='3')
        
        for job in jobs:
            count = Applicant.objects.filter(job=job.id).count()
            total_applicants[job.id] = count

    if request.method == "POST":
        t_app = {}
        if request.POST.get('deptData'):
            deptid=request.POST.get('deptData')
            job_obj=Job.objects.filter(dept=deptid).filter(user=request.user.id, status='3').values()            
            job_obj2=Job.objects.filter(dept=deptid).filter(user=request.user.id, status='3')
            for job in job_obj2:
                count = Applicant.objects.filter(job=job.id).count()
                t_app[job.id] = count
            print(t_app)
            return JsonResponse({'status': 1,'data2': list(job_obj),'total_applicant':t_app})
        else:
            job_obj=Job.objects.filter(user=request.user.id, status='3').values()
            job_obj2=Job.objects.filter(user=request.user.id, status='3')
            for job in job_obj2:
                count = Applicant.objects.filter(job=job.id).count()
                t_app[job.id] = count
            print(t_app)
            return JsonResponse({'status': 1,'data2': list(job_obj),'total_applicant':t_app})

    total_dept = Department.objects.filter(user=request.user.employer).values()    
    context = {
        'total_dept':total_dept,
        'jobs': jobs,
        'total_applicants': total_applicants,
    }
    return render(request, 'ats/archivied_jobs.html', context)

@user_is_employer
def dashboard(request):
    total_app = 0
    total_short = 0
    total_rev = 0
    total_hire = 0
    total_rej = 0
    total_offer = 0
    total_interview = 0
    arr_int = []
    try:
        jobs = Job.objects.filter(user=request.user.id, status='2')
        for job in jobs:
            app = Applicant.objects.filter(job=job.id)
            total_app = total_app + app.count()
            shortlist = Applicant.objects.filter(job=job.id, status='2')
            total_short = total_short + shortlist.count()
            review = Applicant.objects.filter(job=job.id, status='1')
            total_rev = total_rev + review.count()
            hire = Applicant.objects.filter(job=job.id, final_status='1')
            total_hire = total_hire + hire.count()
            rejected = Applicant.objects.filter(job=job.id, final_status='2')
            total_rej = total_rej + rejected.count()
            interview = Interview.objects.filter(job=job.id)
            total_interview = total_interview + interview.count()
            arr_int.extend(interview)
        total_offer = total_hire + total_rej
        # print(app)
        # print(shortlist)
        return render(request, 'ats/dashboard.html', {
            'jobs': jobs,
            'app_count': total_app,
            'app': app,
            'job_count': jobs.count(),
            'shortlist_count': total_short,
            'rev_count': total_rev,
            'hire_count': total_hire,
            'rej_count': total_rej,
            'total_offer': total_offer,
            'int_count': total_interview,
            'arr_int': arr_int
        })
    except:
        return render(request, 'ats/dashboard.html', {
            # 'jobs': jobs,
            'app_count': total_app,
            # 'app': app,
            'job_count': 0,
            'shortlist_count': total_short,
            'rev_count': total_rev,
            'hire_count': total_hire,
            'rej_count': total_rej,
            'total_offer': total_offer,
            'int_count': total_interview,
            # 'arr_int': arr_int
        })

@user_is_employer
def job_post_view(request):
    if request.method == "POST":
        if request.POST.get('tempdata') == "1":
            name = request.POST.get('name')
            role = request.POST.get('role')
            description = request.POST.get('description')
            skill = request.POST.get('skill')
            rolef=Role.objects.get(pk=role)
            temp = Template(user=request.user.employer, name=name, 
            description=description, skill=skill, role=rolef)
            try:
                temp.save()
                id=temp.pk
                return JsonResponse({'status': 1,'id': id})
            except Exception as e:
                return JsonResponse({'status': 0})

        elif request.POST.get('tempGetData'):
            id=request.POST.get('tempGetData')
            temp_val=Template.objects.filter(id=id).values()
            return JsonResponse({'status': 1,'data': list(temp_val)})

        elif request.POST.get('tempDelData'):
            id=request.POST.get('tempDelData')
            temp_val=Template.objects.get(id=id)
            try:
                temp_val.delete();
                return JsonResponse({'status': 1})
            except:
                return JsonResponse({'status': 0})

        elif request.POST.get('tempeditdata'):
            id = request.POST.get('tempeditdata')
            name = request.POST.get('name')
            role = request.POST.get('role')
            description = request.POST.get('description')
            skill = request.POST.get('skill')
            rolef=Role.objects.get(pk=role)
            temp = Template.objects.get(id=id)
            temp.name=name
            temp.description=description
            temp.skill=skill
            temp.role=rolef 
            try:
                temp.save()
                return JsonResponse({'status': 1})
            except Exception as e:
                return JsonResponse({'status': 0})


        elif request.POST.get('saveJob') == "1":
            title = request.POST.get('title')
            role = request.POST.get('role')
            dept = request.POST.get('dept')
            description = request.POST.get('description')
            responsibilities = request.POST.get('responsibilities')
            job_type = request.POST.get('job_type')
            position = request.POST.get('position')
            experince = request.POST.get('experince')
            max_round_no = request.POST.get('max_round_no')
            location = request.POST.get('location')
            work_place = request.POST.get('work_place')
            last_date = request.POST.get('last_date')
            salary = request.POST.get('salary')
            tags = request.POST.get('tags')
            url = request.POST.get('url')
            vacancy = request.POST.get('vacancy')
            qualification = request.POST.get('qualification')
            grade = request.POST.get('grade')
            skill = request.POST.get('skill')
            bonus = request.POST.get('bonus')
            stock = request.POST.get('stock')
            visa = request.POST.get('visa')
            relocation = request.POST.get('relocation')
            working_hour = request.POST.get('working_hour')
            rolef=Role.objects.get(pk=role)
            deptf=Department.objects.get(pk=dept)
            job = Job(user=request.user.employer, title=title, 
                description=description, responsibilities=responsibilities, job_type=job_type, position=position, experince=experince,
                max_round_no=max_round_no, location=location, work_place=work_place, last_date=last_date,
                salary=salary,  tags=tags, url=url, vacancy=vacancy, qualification=qualification,dept=deptf,
                skill=skill,bonus=bonus,stock=stock,visa=visa,relocation=relocation,grade=grade,working_hour=working_hour,role=rolef, status='1'
            )
            try:
                job.save()
                id=job.pk
                job_obj=Job.objects.get(pk=id)
                    
                if request.POST.get('langT1'):
                    title = request.POST.get('langT1')
                    profeciency = request.POST.get('langP1')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()
                if request.POST.get('langT2'):
                    title = request.POST.get('langT2')
                    profeciency = request.POST.get('langP2')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()
                if request.POST.get('langT3'):
                    title = request.POST.get('langT3')
                    profeciency = request.POST.get('langP3')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()
                if request.POST.get('langT4'):
                    title = request.POST.get('langT4')
                    profeciency = request.POST.get('langP4')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()

                return JsonResponse({'status': 1})
            except Exception as e:
                print(e) 
                return JsonResponse({'status': 0})
        
        else:
            title = request.POST.get('title')
            role = request.POST.get('role')
            dept = request.POST.get('dept')
            description = request.POST.get('description')
            responsibilities = request.POST.get('responsibilities')
            job_type = request.POST.get('job_type')
            position = request.POST.get('position')
            experince = request.POST.get('experince')
            max_round_no = request.POST.get('max_round_no')
            location = request.POST.get('location')
            work_place = request.POST.get('work_place')
            last_date = request.POST.get('last_date')
            salary = request.POST.get('salary')
            tags = request.POST.get('tags')
            url = request.POST.get('url')
            vacancy = request.POST.get('vacancy')
            qualification = request.POST.get('qualification')
            grade = request.POST.get('grade')
            skill = request.POST.get('skill')
            bonus = request.POST.get('bonus')
            stock = request.POST.get('stock')
            visa = request.POST.get('visa')
            relocation = request.POST.get('relocation')
            working_hour = request.POST.get('working_hour')
            rolef=Role.objects.get(pk=role)
            deptf=Department.objects.get(pk=dept)
            job = Job(user=request.user.employer, title=title, 
                description=description, responsibilities=responsibilities,job_type=job_type, position=position, experince=experince,
                max_round_no=max_round_no, location=location, work_place=work_place, last_date=last_date,
                salary=salary,  tags=tags, url=url, vacancy=vacancy, qualification=qualification,
                skill=skill,bonus=bonus,stock=stock,visa=visa,relocation=relocation,grade=grade,working_hour=working_hour,role=rolef,dept=deptf,  status='2',publish_date=datetime.datetime.now()
            )
            try:
                job.save()
                id=job.pk
                job_obj=Job.objects.get(pk=id)
                    
                if request.POST.get('langT1'):
                    title = request.POST.get('langT1')
                    profeciency = request.POST.get('langP1')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()
                if request.POST.get('langT2'):
                    title = request.POST.get('langT2')
                    profeciency = request.POST.get('langP2')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()
                if request.POST.get('langT3'):
                    title = request.POST.get('langT3')
                    profeciency = request.POST.get('langP3')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()
                if request.POST.get('langT4'):
                    title = request.POST.get('langT4')
                    profeciency = request.POST.get('langP4')
                    lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                    lang.save()

                return JsonResponse({'status': 1})
            except Exception as e:
                print(e) 
                return JsonResponse({'status': 0})
    
    temp=Template.objects.filter(user=request.user.employer).values()
    dept = Department.objects.filter(user = request.user.employer)
    return render(request, 'ats/jobpost.html', {'temp':temp, 'dept': dept})

@user_is_employer
def job_edit(request,id):
    job=Job.objects.filter(id=id).values()
    job2=Job.objects.filter(id=id)
    lang = Language.objects.filter(user=request.user.employer).filter(job__in=job2).values()
    if request.method == "POST":
        title = request.POST.get('title')
        role = request.POST.get('role')
        dept = request.POST.get('dept')
        description = request.POST.get('description')
        responsibilities = request.POST.get('responsibilities')
        job_type = request.POST.get('job_type')
        position = request.POST.get('position')
        experince = request.POST.get('experince')
        max_round_no = request.POST.get('max_round_no')
        location = request.POST.get('location')
        work_place = request.POST.get('work_place')
        last_date = request.POST.get('last_date')
        salary = request.POST.get('salary')
        tags = request.POST.get('tags')
        url = request.POST.get('url')
        vacancy = request.POST.get('vacancy')
        qualification = request.POST.get('qualification')
        grade = request.POST.get('grade')
        skill = request.POST.get('skill')
        bonus = request.POST.get('bonus')
        stock = request.POST.get('stock')
        visa = request.POST.get('visa')
        relocation = request.POST.get('relocation')
        working_hour = request.POST.get('working_hour')
        rolef=Role.objects.get(pk=role)
        deptf=Department.objects.get(pk=dept)
        job=Job.objects.get(pk=id)
        job.title=title
        job.description=description
        job.responsibilities=responsibilities
        job.job_type=job_type
        job.position=position
        job.experince=experince
        job.max_round_no=max_round_no
        job.location=location
        job.work_place=work_place
        job.last_date=last_date
        job.salary=salary
        job.tags=tags
        job.url=url
        job.vacancy=vacancy
        job.qualification=qualification
        job.skill=skill
        job.bonus=bonus
        job.stock=stock
        job.visa=visa
        job.relocation=relocation
        job.grade=grade
        job.working_hour=working_hour
        job.role=rolef
        job.dept=deptf
        # job = Job(id=id,user=request.user.employer, title=title, 
        #     description=description, responsibilities=responsibilities, qualification_details=qualification_details,
        #     skill_experience=skill_experience, job_type=job_type, position=position, experince=experince,
        #     max_round_no=max_round_no, location=location, work_place=work_place, last_date=last_date,
        #     salary=salary,  tags=tags, url=url, vacancy=vacancy, qualification=qualification,
        #     skill=skill,bonus=bonus,stock=stock,visa=visa,relocation=relocation,grade=grade,working_hour=working_hour,role=rolef,  status='2',publish_date=datetime.datetime.now()
        # )
        try:
            job.save()
            id=job.pk
            job_obj=Job.objects.get(pk=id)
                
            if request.POST.get('langT1'):
                title = request.POST.get('langT1')
                profeciency = request.POST.get('langP1')
                lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                lang.save()
            if request.POST.get('langT2'):
                title = request.POST.get('langT2')
                profeciency = request.POST.get('langP2')
                lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                lang.save()
            if request.POST.get('langT3'):
                title = request.POST.get('langT3')
                profeciency = request.POST.get('langP3')
                lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                lang.save()
            if request.POST.get('langT4'):
                title = request.POST.get('langT4')
                profeciency = request.POST.get('langP4')
                lang =Language(user=request.user.employer,job=job_obj,title=title,profeciency=profeciency)
                lang.save()

            return JsonResponse({'status': 1})
        except Exception as e:
            print(e) 
            return JsonResponse({'status': 0})


    # print(job)
    # print(job2)
    # print(lang)
    dept = Department.objects.filter(user = request.user.employer)
    context={
        'jobs': job,
        'total_lang': lang,
        'dept': dept
    }
    return render(request, 'ats/jobpost_edit.html',context)

@user_is_employer
def job_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        role = request.POST.get('role')
        description = request.POST.get('description')
        responsibilities = request.POST.get('responsibilities')
        qualification_details = request.POST.get('qualification_details')
        skill_experience = request.POST.get('skill_experience')
        job_type = request.POST.get('job_type')
        position = request.POST.get('position')
        experince = request.POST.get('experince')
        max_round_no = request.POST.get('max_round_no')
        location = request.POST.get('location')
        work_place = request.POST.get('work_place')
        last_date = request.POST.get('last_date')
        salary = request.POST.get('salary')
        tags = request.POST.get('tags')
        url = request.POST.get('url')
        vacancy = request.POST.get('vacancy')
        qualification = request.POST.get('qualification')
        job = Job(user=request.user.employer, title=title, 
                description=description, responsibilities=responsibilities, qualification_details=qualification_details,
                skill_experience=skill_experience, job_type=job_type, position=position, experince=experince,
                max_round_no=max_round_no, location=location, work_place=work_place, last_date=last_date,
                salary=salary,  tags=tags, url=url, vacancy=vacancy, qualification=qualification, status='2'
        )
        job.save()

@user_is_employer
def total_applicants(request):
    arr = []
    app = []
    st = ['1','2','3', '4', '5']
    jobs = Job.objects.filter(user=request.user.id, status='2')
    for job in jobs:
        arr.append(job.id)
    if request.method == "GET":
        af = request.GET.get('applicantFilter')
        if af == '0':
            app1 = (Applicant.objects.filter(job__in=arr, status__in = st))
        if af == '1':
            app1 = (Applicant.objects.filter(job__in=arr, status__in = '1'))
           
        elif af == '2':
            app1 = (Applicant.objects.filter(job__in=arr, status__in = '2'))
        elif af == '3':
            app1 = (Applicant.objects.filter(job__in=arr, status__in = '3'))
        elif af == '4':
            app1 = (Applicant.objects.filter(job__in=arr, status__in = '4'))
        elif af == '5':
            app1 = (Applicant.objects.filter(job__in=arr, status__in = '5'))
        elif af == '6':
            app1 = (Applicant.objects.filter(job__in=arr, status__in = '6'))
        else:
            app1 = (Applicant.objects.filter(job__in=arr, status__in = st))
    else:
        app1 = (Applicant.objects.filter(job__in=arr, status__in = st))

    return render(request, 'ats/all-applicatns.html', {'arr': app1})



@user_is_employer
def applicants_short(request):
    arr = []
    st = ['1','2','3', '4', '5']
    jobs = Job.objects.filter(user=request.user.id, status='2')
    for job in jobs:
        arr.append(job.id)

    # app_short = (Applicant.objects.filter(job__in=arr, status='2'))

    if request.method == "GET":
        af = request.GET.get('applicantFilter')
        if af == '0':
            app_short = (Applicant.objects.filter(job__in=arr, status__in = st, final_status='1'))
        if af == '1':
            app_short = (Applicant.objects.filter(job__in=arr, status__in = '1'))
           
        elif af == '2':
            app_short = (Applicant.objects.filter(job__in=arr, status__in = '2'))
        elif af == '3':
            app_short = (Applicant.objects.filter(job__in=arr, status__in = '3'))
        elif af == '4':
            app_short = (Applicant.objects.filter(job__in=arr, status__in = '4'))
        elif af == '5':
            app_short = (Applicant.objects.filter(job__in=arr, status__in = '5'))
        elif af == '6':
            app_short = (Applicant.objects.filter(job__in=arr, status__in = '6'))
        else:
            app_short = (Applicant.objects.filter(job__in=arr, status='2'))
    else:
        app_short = (Applicant.objects.filter(job__in=arr, status='2'))
    return render(request, 'ats/applicants_short.html', {'arr': app_short})


@user_is_employer
def applicants_review(request):
    arr = []
    st = ['1','2','3', '4', '5']
    jobs = Job.objects.filter(user=request.user.id, status='2')
    for job in jobs:
        arr.append(job.id)
    if request.method == "GET":
        af = request.GET.get('applicantFilter')
        if af == '0':
            app_rev = (Applicant.objects.filter(job__in=arr, status__in = st, final_status='1'))
        if af == '1':
            app_rev = (Applicant.objects.filter(job__in=arr, status__in = '1'))
           
        elif af == '2':
            app_rev = (Applicant.objects.filter(job__in=arr, status__in = '2'))
        elif af == '3':
            app_rev = (Applicant.objects.filter(job__in=arr, status__in = '3'))
        elif af == '4':
            app_rev = (Applicant.objects.filter(job__in=arr, status__in = '4'))
        elif af == '5':
            app_rev = (Applicant.objects.filter(job__in=arr, status__in = '5'))
        elif af == '6':
            app_rev = (Applicant.objects.filter(job__in=arr, status__in = '6'))
        else:
            app_rev = (Applicant.objects.filter(job__in=arr, status='1'))
    else:
        app_rev = (Applicant.objects.filter(job__in=arr, status='1'))
    # app_rev = (Applicant.objects.filter(job__in=arr, status='1'))
    return render(request, 'ats/applicants_review.html', {'arr': app_rev})


@user_is_employer
def applicants_hire(request):
    arr = []
    st = ['1','2','3', '4', '5']
    jobs = Job.objects.filter(user=request.user.id, status='2')
    for job in jobs:
        arr.append(job.id)
    if request.method == "GET":
        af = request.GET.get('applicantFilter')
        if af == '0':
            app_hir = (Applicant.objects.filter(job__in=arr, status__in = st, final_status='1'))
        if af == '1':
            app_hir = (Applicant.objects.filter(job__in=arr, status__in = '1'))
           
        elif af == '2':
            app_hir = (Applicant.objects.filter(job__in=arr, status__in = '2'))
        elif af == '3':
            app_hir = (Applicant.objects.filter(job__in=arr, status__in = '3'))
        elif af == '4':
            app_hir = (Applicant.objects.filter(job__in=arr, status__in = '4'))
        elif af == '5':
            app_hir = (Applicant.objects.filter(job__in=arr, status__in = '5'))
        elif af == '6':
            app_hir = (Applicant.objects.filter(job__in=arr, status__in = '6'))
        else:
            app_hir = (Applicant.objects.filter(job__in=arr, final_status='1'))
    else:
        app_hir = (Applicant.objects.filter(job__in=arr, final_status='1'))
    

    # app_hir = (Applicant.objects.filter(job__in=arr, final_status='1'))
    return render(request, 'ats/applicants_hired.html', {'arr': app_hir})

@user_is_employer
def applicants_reject(request):
    arr = []

    st = ['1','2','3', '4', '5']
    jobs = Job.objects.filter(user=request.user.id, status='2')
    for job in jobs:
        arr.append(job.id)
    if request.method == "GET":
        af = request.GET.get('applicantFilter')
        if af == '0':
            app_hld = (Applicant.objects.filter(job__in=arr, status__in = st, final_status='1'))
        if af == '1':
            app_hld = (Applicant.objects.filter(job__in=arr, status__in = '1'))
           
        elif af == '2':
            app_hld = (Applicant.objects.filter(job__in=arr, status__in = '2'))
        elif af == '3':
            app_hld = (Applicant.objects.filter(job__in=arr, status__in = '3'))
        elif af == '4':
            app_hld = (Applicant.objects.filter(job__in=arr, status__in = '4'))
        elif af == '5':
            app_hld = (Applicant.objects.filter(job__in=arr, status__in = '5'))
        elif af == '6':
            app_hld = (Applicant.objects.filter(job__in=arr, status__in = '6'))
        else:
            app_hld = (Applicant.objects.filter(job__in=arr, final_status='2'))
    else:
        app_hld = (Applicant.objects.filter(job__in=arr, final_status='2'))

    


    # app_hld = (Applicant.objects.filter(job__in=arr,final_status='2' ))
    return render(request, 'ats/applicants_reject.html', {'arr': app_hld})

@user_is_employer
def applicant_hold(request):
    arr = []

    st = ['1','2','3', '4', '5']
    jobs = Job.objects.filter(user=request.user.id, status='2')
    for job in jobs:
        arr.append(job.id)
    if request.method == "GET":
        af = request.GET.get('applicantFilter')
        if af == '0':
            app_rej = (Applicant.objects.filter(job__in=arr, status__in = st, final_status='1'))
        if af == '1':
            app_rej = (Applicant.objects.filter(job__in=arr, status__in = '1'))
           
        elif af == '2':
            app_rej = (Applicant.objects.filter(job__in=arr, status__in = '2'))
        elif af == '3':
            app_rej = (Applicant.objects.filter(job__in=arr, status__in = '3'))
        elif af == '4':
            app_rej = (Applicant.objects.filter(job__in=arr, status__in = '4'))
        elif af == '5':
            app_rej = (Applicant.objects.filter(job__in=arr, status__in = '5'))
        elif af == '6':
            app_rej = (Applicant.objects.filter(job__in=arr, status__in = '6'))
        else:
            app_rej = (Applicant.objects.filter(job__in=arr, status='4'))



    # app_rej = (Applicant.objects.filter(job__in=arr, status='4'))
    return render(request, 'ats/applicant_hold.html', {'arr': app_rej})

@user_is_employer
def archieve_job(request, id):
    job = Job.objects.get(id=id)
    print(job.status)
    if job.status == "2":
        Job.objects.filter(id=id).update(status="3")
        return redirect('jobapp:archivied_job_view')
    elif job.status == "3":
        Job.objects.filter(id=id).update(status="2")
        return redirect('jobapp:total_job_view')

@user_is_employer
def close_job(request, id):
    Job.objects.filter(id=id).update(status="4")
    # job.save()
    return redirect('jobapp:total_job_view')

def create_interview(request):
    pass

def edit_interview(request):
    pass

def create_feedback(request):
    pass

def edit_feedback(request):
    pass


def applicant_short_list(request, id):
    Applicant.objects.filter(id=id).update(status='2')
    return redirect('jobapp:applicants_short')

def applicant_in_progress(request, id):
    Applicant.objects.filter(id=id).update(status='3')
    return redirect('jobapp:total_applicants')

def applicant_hired(request, id):
    Applicant.objects.filter(id=id).update(status='5', final_status='1')
    return redirect('jobapp:applicants_hire')

def applicant_rejectd(request, id):
    Applicant.objects.filter(id=id).update(status='6', final_status='2')
    return redirect('jobapp:applicants_reject')

def candidate_profile_view(request, id):
    applicant = Applicant.objects.get(id=id)
    education = Education.objects.filter(user=applicant.user.employee)
    experience = WorkExperience.objects.filter(user=applicant.user.employee)
    
    
    context = {

        'applicant': applicant,
        'education': education,
        'experience': experience,

    }
    return render(request, 'ats/candidate_profile_view.html', context)

@user_is_employer
def account(request):
    emp = EmployerProfile.objects.get(user=request.user)
    ind = Industry.objects.all()
    if request.method == "POST" or 'company_logo' in request.FILES:
        cn = request.POST['company_name']
        cl = request.FILES.get('company_logo')
        cs = request.POST['company_strength']
        ph = request.POST['phone']
        url = request.POST['url']
        des = request.POST['description']
        indus = request.POST['industry']
        ind_obj = Industry.objects.get(id=indus)
        
        try:
           
            
            if request.FILES.get('company_logo'):
                
                try:
                    EmployerProfile.objects.filter(user=request.user.employer).update(company_name=cn, company_strength=cs, description=des, url=url, phone=ph, industry=ind_obj)
                    emp = EmployerProfile.objects.get(user=request.user.employer)
                    emp.company_logo = cl
                    emp.save()
                    img2 = emp.company_logo
                    print('Hello', img2)
                    string = str(img2)
                    return JsonResponse({'status': 1, "data2":string})
                except Exception as e:
                    print(e, 'Hello')
                    return JsonResponse({'status': 1})
            else:
                EmployerProfile.objects.filter(user=request.user.employer).update(company_name=cn, company_strength=cs, description=des, url=url, phone=ph, industry=ind_obj)
                return JsonResponse({'status': 1})
        except Exception as e:
            print(e, 'Hello')
            return JsonResponse({'status': 0})
    context = {
        'emp': emp,
        'ind': ind
    }
    return render(request, 'ats/employer_account.html', context)

@user_is_employer
def organ_account(request):
    dep = Department.objects.filter(user=request.user.employer)
    if request.method == 'POST':
        if request.POST.get("deptDel"):
            id = request.POST.get("deptDel")
            Department.objects.get(id=id).delete()
            return JsonResponse({'status': 1})
        if request.POST.get("title"):
            title = request.POST.get('title')
            dept = Department.objects.filter(user=request.user.employer, title=title)
            # print()
            if dept.count() == 0:
                dept2 = Department.objects.create(user=request.user.employer, title=title)
                return JsonResponse({'status': 1, 'data': dept2.id})
            else:
                return JsonResponse({'status': 0})
        # try:
        #     Department.objects.create(user=request.user.employer, title=title)
        #     dept = Department.objects.filter(user=request.user.employer,title=title)
            
        # except:
        #     return JsonResponse({'status': 0})
        
    context= {
        'dep': dep
    }
    return render(request, 'ats/organisation_account.html', context)

from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

@xframe_options_sameorigin
def job_preview(request,id):
    job = get_object_or_404(Job, id=id)
    job2=Job.objects.filter(id=id)
    tag = job.tags.split(',')
    lang = Language.objects.filter(user=request.user.employer).filter(job__in=job2).values()
    return render(request, 'ats/job-preview.html',{
            'job':job,
            'tag':tag,
            'back':1,
            'total_lang':lang
        })

@xframe_options_sameorigin
def job_preview2(request):
    return render(request, 'ats/job-preview.html')

@user_is_employee
def company_details(request, id):
    detail = EmployerProfile.objects.get(id=id)
    print(detail.user)
    gall = CompanyGallery.objects.filter(user = detail.user)
    jobs = Job.objects.filter(user = detail.user)
    for i in gall:
        print(i.image)
    return render(request, 'jobapp/profile&job.html', {'detail': detail, 'gall': gall,'jobs': jobs})

@user_is_employer
def dashboard_gallery(request):
    gallery = CompanyGallery.objects.filter(user=request.user.employer).values()
    if request.method == "POST" and 'image' in request.FILES:
        title = request.POST.get('title')
        # img = request.FILES
        image = request.FILES.get('image')
        # print(title, image)
        try:
            CompanyGallery.objects.create(user=request.user.employer, title = title, image=image)
            
            gal = CompanyGallery.objects.filter(user=request.user.employer).values()
            
            
            return JsonResponse({'status': 1, "data": list(gal)})
        except:
            return JsonResponse({'status': 0})

    return render(request, 'ats/dashboard_gallery.html', {'gallery': gallery})

    