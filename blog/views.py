from django.shortcuts import render

def index(request):
	context = {
		'pagetitle' : 'Blog',
		'content' : 'ini halaman blog',
	}
	return render(request,'index.html',context)