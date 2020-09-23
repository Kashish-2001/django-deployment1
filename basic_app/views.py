from django.shortcuts import render

# Create your views here.
def index(request):
    index_dict = {'title':"Hello world!!" , 'number': "1" }
    return render(request,'basic_app/index.html',index_dict)

def others(request):
    return render(request,'basic_app/others.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def base(request):
    return render(request,'basic_app/base.html')