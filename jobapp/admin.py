from django.contrib import admin
from .models import *

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('job','timestamp')
    
admin.site.register(Applicant,ApplicantAdmin)
admin.site.register(Interview, InterviewAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title','status','timestamp')

admin.site.register(Job,JobAdmin)

class SKillAdmin(admin.ModelAdmin):
    model = Skill
    ordering = ('-is_primary','name')

class BookmarkJobAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')
admin.site.register(BookmarkJob,BookmarkJobAdmin)
admin.site.register(Curate)
admin.site.register(Location)
admin.site.register(Role)
admin.site.register(Workplace)
admin.site.register(Skill,SKillAdmin)
admin.site.register(Language)
admin.site.register(Department)
admin.site.register(Template)