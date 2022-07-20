from django.contrib import admin
from .models import EmployeeProfile, WorkExperience, Skill, SpokenLanguage, Certificate, Education, Resume

admin.site.register(EmployeeProfile)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(SpokenLanguage)
admin.site.register(Certificate)
admin.site.register(Education)
admin.site.register(Resume)
