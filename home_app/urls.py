
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('ai/', views.AIView, name='AI'),
    path('big-data/', views.BigDataView, name='big_data'),
    path('hrm/', views.ProductHRMView, name='hrm'),
    path('ecommerce/', views.ProductEcommerceView, name='ecommerce'),
    path('soft-qa/', views.ServiceSoftQA, name='soft_qa'),
    path('web-design/', views.ServiceWebDesign, name='web_design'),
    path('contact/', views.ContactView, name='contact'),
    path('ocr/', views.OCRView, name='ocr'),
    path('server-management/', views.ServerManagementView, name='server-management'),
    
]

 