from django.db import models
from django.dispatch import receiver 
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField

from account.models import Employee, Employer

class WorkExperience(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    company = models.CharField(max_length=256, null=True, blank=True)
    year_of_join = models.CharField(max_length=256, null=True, blank=True)
    year_of_end = models.CharField(max_length=256, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    expbody = RichTextField()

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.user.email + self.title

class SpokenLanguage(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    experties = models.CharField(max_length=256, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.user.email + self.title

class Skill(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    experties = models.CharField(max_length=256, null=True, blank=True)
    skill_set = models.CharField(max_length=256, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.user.email + self.title

class Education(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    college = models.CharField(max_length=256, null=True, blank=True)
    year_of_join = models.CharField(max_length=256, null=True, blank=True)
    year_of_end = models.CharField(max_length=256, null=True, blank=True)
    edubody = RichTextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.user.email + self.title

class Certificate(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    company = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.user.email + self.title

class EmployeeProfile(models.Model):
    user = models.OneToOneField(Employee,on_delete=models.CASCADE)
    bio = RichTextField()
    location = models.CharField(max_length=256, null=True, blank=True)
    account_type = models.CharField(max_length=256, null=True, blank=True)
    passing_out_year = models.CharField(max_length=256, null=True, blank=True)
    years_of_experience = models.CharField(max_length=256, null=True, blank=True)
    notice_period = models.CharField(max_length=256, null=True, blank=True)
    s_notice_period = models.BooleanField(default=False)


    def __str__(self):
        return self.user.email

@receiver(post_save, sender=Employee)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        EmployeeProfile.objects.create(user=instance)


@receiver(post_save, sender=Employee)
def save_user_profile(sender, instance, **kwargs):
    instance.employeeprofile.save()

class Resume(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='company/logo/name/', null=True, blank=True)

    def __str__(self):
        return self.title