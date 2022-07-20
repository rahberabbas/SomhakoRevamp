from django.db import models
from account.models import Employer
from ckeditor.fields import RichTextField
from django.dispatch import receiver 
from django.db.models.signals import post_save

class Industry(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.title

class EmployerProfile(models.Model):
    user = models.OneToOneField(Employer,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    description = RichTextField()
    company_logo = models.FileField(upload_to='company/logo/name/', null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE ,null=True, blank=True)
    company_strength = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=Employer)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        EmployerProfile.objects.create(user=instance)


@receiver(post_save, sender=Employer)
def save_user_profile(sender, instance, **kwargs):
    instance.employerprofile.save()

class CompanyGallery(models.Model):
    user = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    image = models.FileField(upload_to='images/company/gallery', null=True, blank=True)

    def __str__(self):
        return self.title