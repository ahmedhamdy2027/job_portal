from django.shortcuts import render, get_object_or_404, redirect
from .models import JobListing, JobApplication, CandidateProfile, Employer
from .forms import JobApplicationForm, JobPostingForm, CandidateProfileForm

def job_list(request):
    jobs = JobListing.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    form = JobApplicationForm()
    return render(request, 'jobs/job_detail.html', {'job': job, 'form': form})

def apply_for_job(request, job_id):
    job = get_object_or_404(JobListing, id=job_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')

        # Create a new JobApplication instance and assign the fields manually
        application = JobApplication()
        application.job = job
        application.name = name
        application.email = email
        application.resume = resume
        application.save()

        return redirect('application_success')
    
    return render(request, 'jops/apply_for_job.html', {'job': job})


def post_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = get_object_or_404(Employer, user=request.user)
            job.save()
            return redirect('job_list')
    else:
        form = JobPostingForm()
    return render(request, 'jobs/post_job.html', {'form': form})

def candidate_profile(request):
    profile, created = CandidateProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = CandidateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_success')
    else:
        form = CandidateProfileForm(instance=profile)
    return render(request, 'jobs/candidate_profile.html', {'form': form})

def application_success(request):
    return render(request, 'jobs/application_success.html')


def profile(request):
    # Logic to get user profile data
    return render(request, 'jobs/profile.html')



def search(request):
    query = request.GET.get('q', '')  # Default to an empty string if 'q' is not provided
    jobs = JobListing.objects.filter(title__icontains=query) if query else JobListing.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})