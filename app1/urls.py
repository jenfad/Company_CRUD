from django.urls import path, re_path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('', views.CompanyList.as_view(), name = 'list'),
    path('<int:pk>', views.CompanyDetail.as_view(), name = 'detail'),
    path('create/', views.CompanyCreate.as_view(), name = 'create'),
    path('update/<int:pk>', views.CompanyUpdate.as_view(), name = 'companyUpdate'),
    path('delete/<int:pk>', views.CompanyDelete.as_view(), name = 'companyDelete'),
]