from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from cardapp.models import Company

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
    model = Company

class CompanyDetailView(DetailView):
    model = Company



