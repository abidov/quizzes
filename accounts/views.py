from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from tests.models import Category, Test, TestResult, UserAnswer
from .models import Profile


class ProfileView(generic.DetailView, generic.UpdateView):
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account-profile')
    model = Profile
    fields = ['phone_number', 'first_name', 'last_name']

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)


def profile_test_result(request):
    test_results = TestResult.objects.filter(user=request.user)
    categories = Category.objects.all()
    return render(request, 'quizzes/profile_test_result.html', locals())


def profile_test_result_detail(request, test_id, test_result_id):
    test = get_object_or_404(Test, pk=test_id)
    test_result = get_object_or_404(TestResult, pk=test_result_id, test=test, user=request.user)
    user_answers = test_result.user_answers.all()
    categories = Category.objects.all()
    return render(request, 'quizzes/profile_test_result_detail.html', locals())
