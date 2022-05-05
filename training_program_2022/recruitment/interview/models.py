from django.db import models

# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议复试'),(u'待定',u'待定'),(u'放弃',u'放弃'))

# 复试面试建议
INTERVIEW_RESULT_TYPE = ((u'建议录用', u'建议录用'),(u'待定',u'待定'),(u'放弃',u'放弃'))

# 候选人学历
DEGREE_TYPE = ((u'本科', u'本科'),(u'硕士',u'硕士'),(u'博士',u'博士'),(u'其他',u'其他'))

# HR终面结果
HR_SCORE_TYPE = (('S','S'),('A','A'),('B','B'),('C','C'))

class Candidate(models.Model):
    # basic info
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name=u'应聘者ID')
    username = models.CharField(max_length=135, verbose_name=u'应聘者姓名')
    city = models.CharField(max_length=135, verbose_name=u'城市')
    phone = models.CharField(max_length=135, verbose_name=u'手机号')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'邮箱')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=u'应聘职位')
    born_address = models.CharField(max_length=135, blank=True, verbose_name=u'出生地')
    gender = models.CharField(max_length=135, blank=True, verbose_name=u'性别')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name=u'候选人信息备注')
    
    # school
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'本科毕业院校')
    master_school = models.CharField(max_length=135, blank=True, verbose_name=u'硕士毕业院校')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'博士毕业院校')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'专业')
    degree = models.CharField(max_length=135, blank=True, verbose_name=u'学历')
    
    # test
    test_score_of_general_ability = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, verbose_name=u'综合能力测试分数')
    paper_score = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, verbose_name=u'笔试分数')
    
    # 1st interview
    first_score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'初试分')
    first_learning_ability = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'学习能力得分')
    first_professional_competency = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'专业能力得分')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'劣势')
    first_result = models.CharField(max_length=256, blank=True, choices=FIRST_INTERVIEW_RESULT_TYPE, verbose_name=u'结果')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'推荐部门')
    first_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'面试官')
    first_remark = models.TextField(max_length=1024, blank=True, verbose_name=u'备注')
    
    #2nd interview
    second_score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'专业复试得分')
    second_learning_ability = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'学习能力得分')
    second_professional_competency = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'专业能力得分')
    second_pursue_of_excellence = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'追求卓越得分')
    second_communication_ability = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'沟通能力得分')
    second_pressure_score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True, verbose_name=u'抗压能力得分')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'劣势')
    second_result = models.CharField(max_length=256, blank=True, choices=INTERVIEW_RESULT_TYPE, verbose_name=u'结果')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'推荐部门')
    second_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'面试官')
    second_remark = models.TextField(max_length=1024, blank=True, verbose_name=u'专业复试备注')
    
    # HR interview
    hr_score = models.CharField(max_length=10, blank=True, choices=HR_SCORE_TYPE, verbose_name=u'HR复试综合等级')
    hr_responsibility = models.CharField(max_length=10, blank=True, choices=HR_SCORE_TYPE, verbose_name=u'HR复试责任心')
    hr_communication_ability = models.CharField(max_length=10, blank=True, choices=HR_SCORE_TYPE, verbose_name=u'HR坦诚沟通')
    hr_logic_ability = models.CharField(max_length=10, blank=True, choices=HR_SCORE_TYPE, verbose_name=u'HR逻辑思维')
    hr_potential = models.CharField(max_length=10, blank=True, choices=HR_SCORE_TYPE, verbose_name=u'HR发展潜力')
    hr_stability = models.CharField(max_length=10, blank=True, choices=HR_SCORE_TYPE, verbose_name=u'HR稳定性')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'劣势')
    hr_result = models.CharField(max_length=256, blank=True, choices=INTERVIEW_RESULT_TYPE, verbose_name=u'HR复试结果')
    hr_interviewer = models.CharField(max_length=256, blank=True, verbose_name=u'HR面试官')
    hr_remark = models.TextField(max_length=1024, blank=True, verbose_name=u'HR复试备注')
    
    # sys info
    creator = models.CharField(max_length=256, blank=True, verbose_name=u'创建人')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modified_date = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name=u'最后修改人')
    
    class Meta:
        db_table = u'candidate'
        verbose_name = u'应聘者'
        verbose_name_plural = u'应聘者'
    
    def __str__(self):
        return self.username