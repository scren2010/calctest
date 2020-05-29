from django.shortcuts import render
from .models import CalcHscode, CalcMeasure, ImageSite
from django.db.models import Q
from . import main

from django.views.generic import ListView, TemplateView

class CalcHscodeView(ListView):
    model = CalcHscode
    modul = ImageSite
    template_name = "pages/index.html"
    context_object_name = 'calchscode'  # Default: object_list
    paginate_by = 5

    def get_queryset(self):
        juery = self.request.GET.get('f')
        query = self.request.GET.get('q')
        if query:
            object_list = CalcHscode.objects.filter(Q(name__icontains=query))
        elif juery:
            object_list = CalcHscode.objects.filter(Q(code__icontains=juery))
        else:
            object_list = CalcHscode.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = {'usd': main.dollar, 'eur': main.euro, 'rub': main.rub, 'tenge': main.tenge, 'day': main.todaydata }
        context['now'] = c
        return context
