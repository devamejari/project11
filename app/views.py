from django.shortcuts import render

# Create your views here.
def deva(request):
    return render(request,'sample1.html')
def meja(request):
    return render(request,'sample2.html')