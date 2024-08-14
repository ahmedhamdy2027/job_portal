from django import forms
from .models import JobApplication, JobListing, CandidateProfile

class JobApplicationForm(forms.ModelForm):
    name = forms.CharField(max_length=255, label="Your Name")
    email = forms.EmailField(label="Your Email")
    resume = forms.FileField(label="Upload Resume")

    class Meta:
        model = JobApplication
        fields = ['cover_letter']

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'description', 'location', 'salary']

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['resume', 'bio']
