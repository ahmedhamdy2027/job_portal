from django.contrib import admin
from .models import JobListing, JobApplication, CandidateProfile, Employer

admin.site.register(JobListing)
admin.site.register(JobApplication)
admin.site.register(CandidateProfile)
admin.site.register(Employer)
