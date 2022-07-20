from django.urls import path
from . import views

app_name = "jobapp"

urlpatterns = [
    path('job_bookmark/', views.job_bookmark, name="job_bookmark"),
    path('job_applied/', views.job_applied, name="job_applied"),
    path('bookmark_delete/', views.bookmark_delete, name="bookmark_delete"),
    path('applied_delete/', views.applied_delete, name="applied_delete"),
    path('jobs/', views.job_list_View, name='job-list'),
    path('cur-delete', views.cur_delete, name="cur_delete"),
    path('cur-edit', views.cur_edit, name="cur_edit"),
    path('cur-view', views.cur_view, name="cur_view"),
    path('can-aply', views.can_aply, name="can_aply"),
    path('', views.home_view, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact-us'),
    path('company-details/<int:id>/', views.company_details, name='company_details'),
    # path('dashboard/employer/', views.naman2, name="naman2"),
    path('job/<int:id>/', views.single_job_view, name='single-job'),
    path('employer/applicant/<int:id>/', views.naman, name="naman"),
    path('dashboard/employer/jobs/', views.total_job_view, name="total_job_view"),
    path('dashboard/employer/archivied_jobs/', views.archivied_job_view, name="archivied_job_view"),
    path('dashboard/employer/', views.dashboard, name="dashboard"),
    path('employer/job/<int:id>/applicants/', views.naman3, name="naman3"),
    path('dashboard/employer/job-post/', views.job_post_view, name="job_post_view"),
    path('dashboard/employer/total_applicants/', views.total_applicants, name="total_applicants"),
    path('dashboard/employer/total_shortlist/', views.applicants_short, name="applicants_short"),
    path('dashboard/employer/total_review/', views.applicants_review, name="applicants_review"),
    path('dashboard/employer/total_hired/', views.applicants_hire, name="applicants_hire"),
    path('dashboard/employer/total_rejected/', views.applicants_reject, name="applicants_reject"),
    path('dashboard/employer/total_rejected/', views.applicants_reject, name="applicants_reject"),
    path('dashboard/employer/total_on_hold/', views.applicant_hold, name="applicant_hold"),
    path('dashboard/employer/candidate_profile_view/<int:id>/', views.candidate_profile_view, name="candidate_profile_view"),
    path('dashboard/employer/account/', views.account, name="account"),
    path('dashboard/employer/account/organisation/', views.organ_account, name="organ_account"),
    path('dashboard/employer/account/dashboard_gallery/', views.dashboard_gallery, name="dashboard_gallery"),
    path('archieve_job/<int:id>/', views.archieve_job, name="archieve_job"),
    path('close_job/<int:id>/', views.close_job, name="close_job"),
    path('applicant_short_list/<int:id>/', views.applicant_short_list, name="applicant_short_list"),
    path('applicant_rejectd/<int:id>/', views.applicant_rejectd, name="applicant_rejectd"),
    path('applicant_hired/<int:id>/', views.applicant_hired, name="applicant_hired"),
    path('applicant_in_progress/<int:id>/', views.applicant_in_progress, name="applicant_in_progress"),
    path('dashboard/employer/jobs/<int:id>/edit/', views.job_edit, name="edit_job"),
    path('dashboard/employer/jobs/<int:id>/preview/', views.job_preview, name="preview_job"),
    path('dashboard/employer/jobs/preview/', views.job_preview2, name="preview_job2"),
]