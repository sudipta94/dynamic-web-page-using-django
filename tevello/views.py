from django.shortcuts import render
from django.http import HttpResponse
from .models import destination
from .models import post

# Create your views here.
def index(request):
    obs=destination.objects.all
    obss=post.objects.all
    return render(request,'index.html',{'obs':obs,'obss':obss})