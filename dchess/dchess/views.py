from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
	print("THIS IS VIEWS.PY IN DCHESS/DCHESS/")
	return render(request, 'index.html')
