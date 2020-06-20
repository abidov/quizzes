from django.views import generic
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy

class ProfileView(generic.DetailView, generic.UpdateView):
    template_name = 'account/profile.html'
    success_url = reverse_lazy('account-profile')
    model = Profile
    fields = ['phone_number', 'first_name', 'last_name']

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
