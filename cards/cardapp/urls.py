from django.urls import path
from cardapp import views

app_name = 'cardapp'

urlpatterns =[
    path('',views.CompanyList.as_view(),name='list'),
    path('<int:pk>',views.CompanyDetailView.as_view(),name='detail')

]

