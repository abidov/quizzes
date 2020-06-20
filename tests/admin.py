from django.contrib import admin
from .models import Test, Question, Answer, TestResult

admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(Answer)
admin.site.register(Question)