from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
        return render(
        request,
        'index.html',
    )
def about(request):
	return render(
		request,
		'about.html',
	)
def products(request):
	return render(
		request,
		'products.html',
	)