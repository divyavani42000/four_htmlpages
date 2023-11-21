from django.shortcuts import render

# Create your views here.
def divya(request):
    return render(request,'divya.html')

def yoyo(request):
    return render(request,'yoyo.html')
def mom(request):
    return render(request,'mom.html')
def dad(request):
    return render(request,'dad.html')