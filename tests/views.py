from django.views import View
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import Test, Question, Answer, TestResult
from .forms import TestCreateForm, TestUpdateForm, QuestionCreateForm, AnswerCreateForm


@login_required(login_url='/accounts/login/')
def my_test_list(request):
    create_form = TestCreateForm()
    update_form = TestUpdateForm()
    tests = Test.objects.filter(user=request.user)
    return render(request, 'quizzes/my_quiz_list.html', locals())


@login_required(login_url='/accounts/login/')
def my_test_create(request):
    if request.method == 'POST':
        form = TestCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            test_instance = form.save()
            detail_url = reverse('question-list', kwargs={'test_id': test_instance.id})
            update_url = reverse('my-test-update', kwargs={'test_id': test_instance.id})
            delete_url = reverse('my-test-delete', kwargs={'test_id': test_instance.id})
            serialized_instance = serializers.serialize('json', [test_instance])
            return JsonResponse({'new_test': serialized_instance, 'update_url': update_url, 'detail_url': detail_url, 'delete_url': delete_url}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'not ajax request'}, status=400)


@login_required(login_url='/accounts/login/')
def my_test_update(request, test_id):
    test = get_object_or_404(Test, pk=test_id, user=request.user)
    if request.method == 'GET':
        return JsonResponse({'test_title': test.title, 'test_description': test.description, 'test_is_active': test.is_active}, status=200)
    elif request.method == 'POST':
        form = TestUpdateForm(request.POST, request.FILES, instance=test)
        if form.is_valid():
            form.save()
        return redirect('my-test-list')


@login_required(login_url='/accounts/login/')
def my_test_delete(request, test_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id, user=request.user)
        test.delete()
        return JsonResponse({'result': 'ok'}, status=200)
    return JsonResponse({'error': 'not ajax request'}, status=400)


@login_required(login_url='/accounts/login/')
def question_list(request, test_id):
    test = get_object_or_404(Test, pk=test_id, user=request.user)
    question_form = QuestionCreateForm()
    question_update_form = QuestionCreateForm()
    answer_form = AnswerCreateForm()
    answer_update_form = AnswerCreateForm()
    return render(request, 'quizzes/my_quiz_detail.html', {'test': test,
                                                           'question_form': question_form,
                                                           'question_update_form': question_update_form,
                                                           'answer_form': answer_form,
                                                           'answer_update_form': answer_update_form,
                                                           })


@login_required(login_url='/accounts/login/')
def question_create(request, test_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id, user=request.user)
        question_form = QuestionCreateForm(request.POST)
        answer_form = AnswerCreateForm(request.POST)
        if question_form.is_valid():
            question_form.instance.test = test
            question_instance = question_form.save()
            test.questions_id.append(question_instance.id)
            test.save()
            delete_url = reverse('question-delete', kwargs={'test_id': test_id, 'question_id': question_instance.id})
            update_url = reverse('question-update', kwargs={'test_id': test_id, 'question_id': question_instance.id})
            answer_create_url = reverse('answer-create', kwargs={'test_id': test_id, 'question_id': question_instance.id})
            serialized_instance = serializers.serialize('json', [question_instance])
            return JsonResponse({'new_question': serialized_instance, 'delete_url': delete_url, 'update_url': update_url, 'answer_create_url': answer_create_url}, status=200)
        else:
            return JsonResponse({'error': question_form.errors}, status=400)
    return JsonResponse({'error': 'not ajax request'}, status=400)


@login_required(login_url='/accounts/login/')
def question_update(request, test_id, question_id):
    test = get_object_or_404(Test, pk=test_id, user=request.user)
    question = get_object_or_404(Question, pk=question_id, test=test)
    if request.method == 'GET':
        return JsonResponse({'question_problem': question.problem}, status=200)
    elif request.method == 'POST':
        question_form = QuestionCreateForm(request.POST, instance=question)
        if question_form.is_valid():
            question_form.save()
            return redirect('question-list', test_id)
        return render(request, 'quizzes/question_update.html', locals())


@login_required(login_url='/accounts/login/')
def question_delete(request, test_id, question_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id, user=request.user)
        question = get_object_or_404(Question, pk=question_id, test=test)
        question.delete()
        test.questions_id.remove(question_id)
        test.save()
        return JsonResponse({'result': 'ok'}, status=200)
    return JsonResponse({'error': 'not ajax request'}, status=400)


@login_required(login_url='/accounts/login/')
def answer_create(request, test_id, question_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id, user=request.user)
        question = get_object_or_404(Question, pk=question_id)
        if question in test.questions.all():
            question = get_object_or_404(Question, pk=question_id, test=test)
            answer_form = AnswerCreateForm(request.POST)
            if answer_form.is_valid():
                answer_form.instance.question = question
                answer_instance = answer_form.save()
                delete_url = reverse('answer-delete', kwargs={'test_id': test_id, 'answer_id': answer_instance.id})
                update_url = reverse('answer-update', kwargs={'test_id': test_id, 'answer_id': answer_instance.id})
                serialized_instance = serializers.serialize('json', [answer_instance])
                return JsonResponse({'new_answer': serialized_instance, 'delete_url': delete_url, 'update_url': update_url})
            else:
                return JsonResponse({'error': answer_form.errors}, status=400)
    return JsonResponse({'error': 'not ajax request'})


@login_required(login_url='/accounts/login/')
def answer_update(request, test_id, answer_id):
    if request.method == 'GET':
        test = get_object_or_404(Test, pk=test_id, user=request.user)
        questions = test.questions.all()
        answer = get_object_or_404(Answer, pk=answer_id)
        if answer.question in questions:
            return JsonResponse({'answer_text': answer.text, 'answer_is_correct': answer.is_correct}, status=200)
    elif request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id, user=request.user)
        questions = test.questions.all()
        answer = get_object_or_404(Answer, pk=answer_id)
        if answer.question in questions:
            form = AnswerCreateForm(request.POST, instance=answer)
            if form.is_valid():
                form.save()
                return redirect('question-list', test_id)
            return render(request, 'quizzes/answer_update.html', locals())


@login_required(login_url='/accounts/login/')
def answer_delete(request, test_id, answer_id):
    if request.method == 'POST':
        test = get_object_or_404(Test, pk=test_id, user=request.user)
        questions = test.questions.all()
        answer = get_object_or_404(Answer, pk=answer_id)
        for question in questions:
            if answer in question.answers.all():
                answer.delete()
                return JsonResponse({'result': 'ok'}, status=200)
        return JsonResponse({'result': 'not your test'}, status=400)
    return JsonResponse({'error': 'not ajax request'}, status=400)


@login_required(login_url='/accounts/login/')
def check_answer(request, answer_id):
    if request.is_ajax() and request.method == 'GET':
        answer = get_object_or_404(Answer, pk=answer_id)
        if answer.is_correct:
            return JsonResponse({'is_correct': True})
        return JsonResponse({'is_correct': False})
    return JsonResponse({'error': 'not ajax request'}, status=400)


def tests_list(request):
    tests = Test.objects.filter(is_active=True)
    return render(request, 'quizzes/quiz_list.html', locals())


def test_detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id, is_active=True)
    return render(request, 'quizzes/quiz_detail.html', locals())