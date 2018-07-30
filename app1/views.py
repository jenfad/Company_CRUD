from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['inject']='''Click on "Companies" above to see 
        a list of companies initially generated using the faker library.'''
        return context

class CBView(View):
    def get(self, request):
        return HttpResponse("Using Class-Based Views")

class CompanyList(ListView):
    model = models.Company
    # by default returns list named company_list
    # can change list name by using context_object_name
    context_object_name = 'companies'


class CompanyDetail(DetailView):
    model = models.Company
    template_name = 'app1/company_detail.html'
    #default name of what returns is company
    context_object_name = 'company_detail'

class CompanyCreate(CreateView):
    fields = ('name','headquarters', 'industry', 'founding_year')
    model = models.Company

class CompanyUpdate(UpdateView):
    fields = ('headquarters', 'industry', 'founding_year')
    model = models.Company
    success_url = reverse_lazy('app1:list')

class CompanyDelete(DeleteView):
    model = models.Company
    success_url = reverse_lazy('app1:list')


