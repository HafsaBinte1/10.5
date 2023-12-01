from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'Contact.html')
def nav(request):
    return render(request, 'nav.html')
