from django.urls import include, path

from . import views
from .views import CalcFormsView

urlpatterns = [
    path('', CalcFormsView.as_view(), name='home'),
]