from django.shortcuts import render
from tests.models import Category


def index(request):
    categories = Category.objects.all()
    return render(request, 'quizzes/index.html', locals())