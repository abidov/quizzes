from django.contrib import admin
from .models import Test, Question, Answer, TestResult, Category, UserAnswer


class QuestionInline(admin.StackedInline):
    model = Question


class AnswerInline(admin.StackedInline):
    model = Answer


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('category', 'user', 'created', 'is_active', 'image')
    list_filter = ('category', 'user', 'created', 'is_active')
    list_display_links = ('category', 'user', 'image', )
    inlines = (QuestionInline,)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'problem')
    list_filter = ('test', 'problem')
    list_display_links = ('test',)
    inlines = (AnswerInline,)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('question', 'text', 'is_correct')
    list_display_links = ('question',)


admin.site.site_header = 'Test Administration'
admin.site.register(TestResult)
admin.site.register(Category)
admin.site.register(UserAnswer)
