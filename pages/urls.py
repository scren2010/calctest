from django.urls import path
from .views import CalcHscodeView

from . import views

urlpatterns = [
    path("", CalcHscodeView.as_view(), name='index'),
]
