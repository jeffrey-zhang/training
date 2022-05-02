from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from jobs.models import Cities, Job, JobTypes


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}

    for job in job_list:
        job.job_city = Cities[job.job_city]
        job.job_type = JobTypes[job.job_type]

    return HttpResponse(template.render(context, request))
