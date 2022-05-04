from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader

from jobs.models import Cities, Job, JobTypes


def joblist(request):
    job_list = Job.objects.order_by('job_type')

    # <1> 函数方式render 页面
    # <1>joblist.html 获取到template中
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}  # <1>在html中定义了block content

    for job in job_list:
        job.job_city = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    # return HttpResponse(template.render(context)) # <1> render函数将context中的内容渲染到template中

    # <2> 方法2 直接渲染页面
    return render(request, 'joblist.html', {'job_list': job_list})


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.job_city = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")

    return render(request, 'job.html', {'job': job})
