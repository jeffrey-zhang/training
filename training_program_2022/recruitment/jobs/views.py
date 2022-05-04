from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader

from jobs.models import Cities, Job, JobTypes


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}

    for job in job_list:
        job.job_city = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))

def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.job_city = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    
    return render(request, 'job.html', {'job': job})