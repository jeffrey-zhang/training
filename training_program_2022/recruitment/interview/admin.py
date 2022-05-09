from asyncore import write
from urllib import response
from django.contrib import admin
from django.http import HttpResponse
from interview.models import Candidate

import csv
from datetime import datetime

exportable_fields = (
    "username", "city", "bachelor_school", "test_score_of_general_ability", "paper_score",
    "first_score", "first_result", 'first_interviewer',
    'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'last_editor')


def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}-{}.csv'.format(
        modeladmin.model._meta.model_name, datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    field_list = exportable_fields

    write = csv.writer(response, dialect='excel')
    # BOM (optional...Excel needs it to open UTF-8 file properly)
    write.writerow('\ufeff')
    write.writerow([
        queryset.model._meta.get_field(f).verbose_name for f in field_list
    ])

    for obj in queryset:
        csv_line_values = []
        for field in field_list:
            field_value = queryset.model._meta.get_field(
                field).value_from_object(obj)
            csv_line_values.append(field_value)
        write.writerow(csv_line_values)

    return response


export_model_as_csv.short_description = "导出为CSV文件"


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    actions = [export_model_as_csv]

    list_display = (
        "username", "city", "bachelor_school", "test_score_of_general_ability", "paper_score",
        "first_score", "first_result", 'first_interviewer',
        'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'last_editor'
    )

    list_filter = (
        'city', 'first_result', 'second_result', 'hr_result', 'first_interviewer', 'second_interviewer', 'hr_interviewer',
    )

    search_fields = (
        "username", "phone", 'email', 'bachelor_school',
    )

    ordering = (
        'hr_result', 'first_result', 'second_result',
    )

    fieldsets = (
        ('基本信息', {"fields": ("userid", ("username", "city", "phone"), ("email", "apply_position", "born_address"), ("gender", "candidate_remark"),
         ("bachelor_school", "master_school", "doctor_school"), ("major", "degree"), ("test_score_of_general_ability", "paper_score"),), }),
        ('第一轮面试记录', {'fields': (("first_score", "first_learning_ability", "first_professional_competency"), "first_advantage",
         "first_disadvantage", ("first_result", "first_recommend_position", "first_interviewer"), "first_remark",)}),
        ('第二轮面试记录', {'fields': (("second_score", "second_learning_ability", "second_professional_competency"), ("second_pursue_of_excellence", "second_communication_ability",
         "second_pressure_score"), "second_advantage", "second_disadvantage", ("second_result", "second_recommend_position", "second_interviewer"), "second_remark",)}),
        ('HR面试记录', {'fields': (("hr_score", "hr_responsibility", "hr_communication_ability"), ("hr_logic_ability",
         "hr_potential", "hr_stability"), "hr_advantage", "hr_disadvantage", ("hr_result", "hr_interviewer"), "hr_remark",)}),
    )


admin.site.register(Candidate, CandidateAdmin)
