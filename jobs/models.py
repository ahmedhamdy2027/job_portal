from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()

    def __str__(self):
        return self.company_name

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_by = models.ForeignKey(Employer, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class JobApplication(models.Model):
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()

    def __str__(self):
        return f'{self.candidate} applied for {self.job}'
