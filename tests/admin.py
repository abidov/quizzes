from django.contrib import admin
from .models import Test, Question, Answer, TestResult, Category

admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Category)