from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.dispatch import receiver 
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import Employee, Employer
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


job_status = (
    ('1', "Drafted"),
    ('2', "Active"),
    ('3', "Arcived"),
    ('4', "Close"),
)

job_type = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
    ('4', "Contract"),
)

job_exp = {
    ('1', "0-2 Yrs"),
    ('2', "2-4 Yrs"),
    ('3', "5+ Yrs"),
}

applicant_status = {
    ('1', "In-Review"),
    ('2', "Shortlist"),
    ('3', "In-Progress"),
    ('4', "On-Hold"),
    ('5', "Completed"),
    ('6', "Rejected"),
}

applicant_finalstatus = {
    ('1', "Hire"),
    ('2', "Reject"),
}

interview_status = {
    ('1', "Hire"),
    ('2', "Reject"),
    ('3', "Hold"),
}

interview_second_status = {
    ('1', "Passed"),
    ('2', "Reject"),
    ('3', "On-Hold"),
}

class Location(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Workplace(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
    def __str__(self):
        if self.is_primary:
            return self.name+" ("+str(self.role)+") (Primary)"
        else:
            return self.name+" ("+str(self.role)+")"

POSITION = (
    ('1', "Fresher"),
    ('2', "Junior"),
    ('3', "Senior"),
    ('4', "Mid Carrer"),
    ('5', "Executive"),
)     

WORKPLACE = (
    ('1', "Remote"),
    ('2', "Hybrid"),
    ('3', "On-Site"),
)  
    

GRADE = (
    ('1', "High Distinction"),
    ('2', "Distinction"),
    ('3', "Credit"),
    ('4', "Pass"),
)  
VISA = (
    ('1', "Yes"),
    ('2', "No"),
)

class Department(models.Model):
    user =  models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title
    

class Job(models.Model):
    
    user = models.ForeignKey(Employer, related_name='Employer', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = RichTextField(null=True, blank=True)
    responsibilities = RichTextField(null=True, blank=True)
    # qualification_details = RichTextField(null=True, blank=True)
    # skill_experience = RichTextField(null=True, blank=True)
    vacancy = models.CharField(max_length=30, blank=True, null=True)
    working_hour = models.CharField(max_length=30, blank=True, null=True)
    qualification = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(choices=POSITION, max_length=1, blank=True)
    work_place = models.CharField(choices=WORKPLACE, max_length=1, blank=True)
    tags = models.CharField(max_length=2000,blank=True,help_text="comma for new tags")
    skill = models.CharField(max_length=2000,blank=True,help_text="comma for new tags",null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    job_type = models.CharField(choices=job_type, max_length=1, blank=True, null=True)
    experince = models.CharField(choices=job_exp, max_length=1, blank=True)
    dept = models.ForeignKey(Department,related_name='dept', on_delete=models.CASCADE,blank=True, null=True)
    grade = models.CharField(choices=GRADE, max_length=1, blank=True, null=True)
    role = models.ForeignKey(Role,related_name='Role', on_delete=models.CASCADE,blank=True, null=True)
    salary = models.CharField(max_length=30, blank=True)
    bonus = models.CharField(max_length=30, blank=True)
    stock = models.CharField(max_length=30, blank=True)
    visa = models.CharField(choices=VISA, max_length=1, blank=True, null=True)
    relocation = models.CharField(choices=VISA, max_length=1, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    last_date = models.DateField()
    max_round_no= models.IntegerField(default=0,validators=[MinValueValidator(0)])
    status = models.CharField(choices=job_status, max_length=1, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True,null=True)


    def str(self):
        return self.title

LANGUAGE_PROFECIENCY = (
    ('1', "Beginner"),
    ('2', "Intermediate"),
    ('3', "Advance"),
)   

class Language(models.Model):

    user = models.ForeignKey(Employer, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    profeciency = models.CharField(choices=LANGUAGE_PROFECIENCY, max_length=1, blank=True, null=True)

    def _str_(self):
        return self.job.title + " " + self.title
 


class Applicant(models.Model):

    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    source_of_application = models.CharField(max_length=2000,blank=True)
    status = models.CharField(choices=applicant_status, max_length=1, blank=True)
    final_status = models.CharField(choices=applicant_finalstatus, max_length=1, blank=True)
    followup_count= models.IntegerField(default=0,validators=[MinValueValidator(0)])
    followup_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

class Interview(models.Model):

    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(choices=interview_status, max_length=1, blank=True)
    second_status = models.CharField(choices=interview_second_status, max_length=1, blank=True)
    round_no= models.IntegerField(default=0,validators=[MinValueValidator(0)])
    comment = models.CharField(max_length=2000,blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    interview_date = models.DateField(blank=True,null=True)
    interview_start_time = models.TimeField(blank=True,null=True)
    interview_end_time = models.TimeField(blank=True,null=True)

    def __str__(self):
        return self.job.title


class BookmarkJob(models.Model):

    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title

class Curate(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="",blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    skill = models.CharField(max_length=100, null=True, blank=True)
    workplace = models.CharField(max_length=100, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    news_letter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email+"."+self.name

class Template(models.Model):
    user = models.ForeignKey(Employer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="",blank=True)
    description = RichTextField(null=True, blank=True)
    role = models.ForeignKey(Role,related_name='Dept', on_delete=models.CASCADE,blank=True, null=True)
    skill = models.CharField(max_length=2000,blank=True,help_text="comma for new tags",null=True)
    
    def __str__(self):
        return self.user.email+"."+self.name