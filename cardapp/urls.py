from django.urls import path
from cardapp import views

app_name = 'cardapp'

urlpatterns =[
    path('',views.CompanyList.as_view(),name='list'),
    path('<int:pk>',views.CompanyDetailView.as_view(),name='detail'),
    path('create/',views.CompanyCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.CompanyUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.CompanyDeleteView.as_view(),name='delete')


]

