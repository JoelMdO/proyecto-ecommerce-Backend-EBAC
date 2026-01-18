from typing import Any
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import UserRegistrationModelForm

class FormsView(LoginRequiredMixin, TemplateView):
    template_name = "forms/forms.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)

        initial_data = {
        "username": "Your username",
        "password": "Your password",
        "email": "Your email",
        }

        form = UserRegistrationModelForm(self.request.POST or None, initial=initial_data)
        context['form'] = form
        return context

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any):
        initial_data = {
            "username": "Your username",
            "password": "Your password", 
            "email": "Your email",
        }
        
        form = UserRegistrationModelForm(self.request.POST, initial=initial_data)
        if form.is_valid():
            print(form.cleaned_data)  # <--- Imprime on docker console
            form.save()  
        
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)
