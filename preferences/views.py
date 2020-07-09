from django.shortcuts import render
from django.views.generic import FormView
from .forms import PreferenceModelForm
from django.contrib import messages

class MyPreferenceFormView(FormView):
    form_class = PreferenceModelForm
    template_name = 'preferences/main.html'

    def get_success_url(self):
        return  self.request.path 

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Saved successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Ups..something went wrong')
        return super().form_invalid(form)