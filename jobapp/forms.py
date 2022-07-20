from account.models import Employer
from django import forms
from employer.models import CompanyGallery

class GalleryImageUpload(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=Employer.objects.all(),
            widget=forms.HiddenInput())
    class Meta:
        model = CompanyGallery
        fields = ( 'title', 'image', 'user')
       