from django.urls import path
from .views import SignUpView, MemberCodeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("membercode/", MemberCodeView.as_view(), name="member-code")
]