from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.conf import settings


from .forms import CustomUserCreationForm, MemberCodeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class MemberCodeView(FormView):
    form_class = MemberCodeForm
    success_url = reverse_lazy("home")
    template_name = "membercode.html"

    def form_valid(self, form):
        if form.cleaned_data['membership_code'] == settings.MEMBER_CODE:
            self.request.user.member = True
            self.request.user.save()
        return super().form_valid(form)
