from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ViewAccountProfile(generic.DetailView):
    template_name = 'users/viewAccount.html'
    model = CustomUser
    context_object_name = "user"

    def get_object(self):
        return CustomUser.objects.get(id=self.request.user.id)
