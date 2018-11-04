from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Players

def index(request):
	players = Players.objects.all().order_by('-total')
	mylist = zip(players, range(1,61))
	return render(request,'index.html',{'mylist':mylist})
