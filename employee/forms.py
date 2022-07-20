from django import forms
from .models import EmployeeProfile,Education,WorkExperience,Certificate,Skill,SpokenLanguage
from account.models import Employee
from ckeditor.widgets import CKEditorWidget

import datetime
YEARS_CHOICE = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEARS_CHOICE.append((r,r))
YEARS_CHOICE.append(("Present","Present"))

class EmployeeProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ["first_name", "last_name", 'mobile']

class EmployeeProfile2EditForm(forms.ModelForm):

    class Meta:
        model = EmployeeProfile
        fields = ["bio", "location", 'account_type', 'passing_out_year', 'years_of_experience']

class EducationAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EducationAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "School/College Name :"
        self.fields['college'].label = "University Name :"
        self.fields['year_of_join'].label = "Start Year :"
        self.fields['year_of_end'].label = "End Year :"
        self.fields['edubody'].label = "About :"
    class Meta:
        model = Education
        fields = ["title", "college", "year_of_join", 'year_of_end', 'edubody']
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'id': 'eduTitleID', 'placeholder': 'Enter School/College Name', 'required': 'required'}),
            'college': forms.TextInput(attrs= {'class': 'form-control', 'id': 'eduCollegeID', 'placeholder': 'Enter University Name'}),
            'year_of_join': forms.Select(choices=YEARS_CHOICE,attrs= {'class': 'form-control', 'id': 'eduSYearID', 'placeholder': 'Enter Start Year'}),
            'year_of_end': forms.Select(choices=YEARS_CHOICE ,attrs= {'class': 'form-control', 'id': 'eduEYearID', 'placeholder': 'Enter End Year'}),
            # 'body': forms.TextInput(attrs= {'class': 'form-control', 'id': 'eduAboutID', 'placeholder': 'Enter About'}),
            'edubody': CKEditorWidget(attrs={'id':'eduBodyID',})
        }


class ExperienceAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExperienceAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Role :"
        self.fields['company'].label = "Company Name :"
        self.fields['year_of_join'].label = "Start Year :"
        self.fields['year_of_end'].label = "End Year :"
        self.fields['expbody'].label = "About :"
    class Meta:
        model = WorkExperience
        fields = ["title", "company", "year_of_join", 'year_of_end', 'expbody']
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'id': 'expTitleID', 'placeholder': 'Enter Role'}),
            'company': forms.TextInput(attrs= {'class': 'form-control', 'id': 'expCompanyID', 'placeholder': 'Enter Company Name'}),
            'year_of_join': forms.Select(choices=YEARS_CHOICE,attrs= {'class': 'form-control', 'id': 'expSYearID',}),
            'year_of_end': forms.Select(choices=YEARS_CHOICE, attrs= {'class': 'form-control', 'id': 'expEYearID',}),
            # 'body': forms.TextInput(attrs= {'class': 'form-control', 'id': 'eduAboutID', 'placeholder': 'Enter About'}),
            'expbody': CKEditorWidget()
        }

class CertificateAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CertificateAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Role :"
        self.fields['company'].label = "Company Name :"
        self.fields['url'].label = "URL :"
    class Meta:
        model = Certificate
        fields = ["title", "company", "url"]
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'id': 'cerTitleID', 'placeholder': 'Enter Title'}),
            'company': forms.TextInput(attrs= {'class': 'form-control', 'id': 'cerCompanyID', 'placeholder': 'Enter Company Name'}),
            'url': forms.TextInput(attrs= {'class': 'form-control', 'id': 'cerURLID', 'placeholder': 'Enter URL'}),
        }

Skill_PROFECIENCY = [
    ('Beginner',"Beginner"), ('Intermediate','Intermediate') ,('Advance',"Advance")
]

Skill_SET = [
    ('Primary',"Primary"), ('Secondary','Secondary')
]

class SkillsAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SkillsAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Skill :"
        self.fields['experties'].label = "Profeciency :"
        self.fields['skill_set'].label = "Skill Set :"
    class Meta:
        model = Skill
        fields = ["title", "experties", "skill_set"]
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'id': 'sklTitleID', 'placeholder': 'Enter Skill'}),
            'experties': forms.Select(choices=Skill_PROFECIENCY ,attrs= {'class': 'form-control', 'id': 'sklexpertiesID'}),
            'skill_set': forms.Select(choices=Skill_SET,attrs= {'class': 'form-control', 'id': 'sklsetID'}),
        }

LANGUAGE_PROFECIENCY = [
    ('Beginner',"Beginner"), ('Intermediate','Intermediate') ,('Advance',"Advance")
]

class LanguageAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LanguageAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Language :"
        self.fields['experties'].label = "Profeciency :"
    class Meta:
        model = SpokenLanguage
        fields = ["title", 'experties']
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'id': 'lngTitleID', 'placeholder': 'Enter Language','required': 'required'}),
            'experties': forms.Select(choices=LANGUAGE_PROFECIENCY ,attrs= {'class': 'form-control', 'id': 'lngexpertiesID',}),
        }