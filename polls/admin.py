from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('文本详情', {'fields': ['question_text']}),
        ('日期信息', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]

    # 显示详情列控制
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 显示过滤字段控制
    list_filter = ['pub_date']

    # 搜索字段控制
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
