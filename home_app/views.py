from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request,'home_app/index.html')

def AboutView(request):
    return render(request,'home_app/about.html')

def AIView(request):
    return render(request,'home_app/artificial-intelligence-ai.html')

def BigDataView(request):
    return render(request,'home_app/big-data-engineering.html')

def ProductHRMView(request):
    return render(request,'home_app/hrm-new.html')

def ProductEcommerceView(request):
    return render(request,'home_app/multi-vendor-e-commerce-website.html')

def ServiceSoftQA(request):
    return render(request,'home_app/software-apps-qa.html')

def ServiceWebDesign(request):
    return render(request,'home_app/web-design-development.html')