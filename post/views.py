from django.shortcuts import render

# Create your views here.
from .models import Post
def index(request):
	posts = Post.objects.all()
	context = {
		'pagetitle':'Halaman post',
		'content' : 'content postingan halaman post',
		'post' : posts
	}
	return render(request,'post/index.html',context)