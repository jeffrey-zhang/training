from django.db import models
from django.contrib.auth.models import User

JobTypes = [
    (0, '技术类'),
    (1, '产品类'),
    (2, '运营类'),
    (3, '设计类'),
]

Cities = [
    (0, '北京'),
    (1, '上海'),
    (2, '深圳'),
]


class Job(models.Model):
    job_type = models.SmallIntegerField(
        blank=False, choices=JobTypes, verbose_name="职位列表")
    job_name = models.CharField(
        max_length=250, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(
        blank=False, choices=Cities, verbose_name="工作地点")
    job_reponsiblity = models.TextField(
        blank=False, max_length=1024, verbose_name="职责描述")
    job_requirement = models.TextField(
        blank=False, max_length=1024, verbose_name="职位要求")
    creator = models.ForeignKey(
        User, verbose_name="创建者", null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)
    
    class Meta:
        verbose_name = "职位"
        verbose_name_plural = "职位"
        ordering = ['-created_date']
