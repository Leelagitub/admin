from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from cardapp.models import Company
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     return render(request,'index.html')

# class myclass(View):
#     def get(self,request):
#         return HttpResponse('This is a class based view')
    
class myclass(TemplateView):
    template_name = "index.html"    

#  def index(request):
#     res = Company.objects.all()
#     return render(request,'index.html',{'res':res})

class CompanyList(ListView):
    context_object_name = 'mycompanylist'
    model = Company

class CompanyDetailView(DetailView):
    context_object_name = 'company_detail'
    model = Company

class CompanyCreateView(CreateView):
    fields = ['name','ceo','origin']
    model = Company

class CompanyUpdateView(UpdateView):
    fields = ['name','ceo']
    model = Company

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('cardapp:list')