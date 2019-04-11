from django.shortcuts import render
from django.views import View

# Create your views here.
from blog.models import Blog


class IndexView(View):
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        return render(request, 'index.html', {
            'all_blog': all_blog,
        })


class AboutMeView(View):
    def get(self, request):
        return render(request, 'about.html')


class FirstPage(View):
    def get(self, request):
        return render(request, 'index.html')
