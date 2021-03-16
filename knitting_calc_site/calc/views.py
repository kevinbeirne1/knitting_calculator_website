from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView

from .forms import CalcForm

def home(request):
    return HttpResponse("You're at the home page")


class CalcFormsView(FormView):
    # specify form to use
    form_class = CalcForm

    # specify name of the template
    template_name = 'calc/calc_model_form.html'
