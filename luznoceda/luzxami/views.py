from django.shortcuts import render
from django.http import HttpResponse
def luz(request):
    return render(request, 'moy.html', context=None )
def amity(request):
    return render(request, 'loy.html', context=None) 
def hoşgeldiniz(request):
    return HttpResponse('https://github.com/Moy247')
def youtube(request):
    return HttpResponse('https://www.youtube.com/@Mahryldrmofficial')
# Create your views here.
