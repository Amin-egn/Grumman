# django
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
# internal
from panel.views import BaseView
from .forms import RegisterForm


def login_view(request):
    return render(request, 'login.html')


class RegisterView(BaseView):
    """Register View"""
    TEMPLATE = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return self.render(request, form=form)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        return self.render(request, form=form)
