from django.contrib import admin
from jobs.models import Job


class JobAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('job_name', 'job_type', 'job_city',
                    'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change) -> None:
        obj.creator = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
