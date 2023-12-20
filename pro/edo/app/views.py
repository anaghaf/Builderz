# from django.shortcuts import render

# Create your views here.
# views.py
\
from django.shortcuts import render
from .models import Video, Audio
from .models import Userreg
from django.http import HttpResponse



def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def audio_list(request):
    audios = Audio.objects.all()
    return render(request, 'audio_list.html', {'audios': audios})

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

from django.contrib.auth.hashers import check_password

def login(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    print(email)
    if email == 'admin@gmail.com' and password == '09876':
        return redirect('dash')     
    elif email == 'kumar@gmail.com' and password == '12345':
        return redirect('ind')  
    return render(request, 'login.html')



from django.shortcuts import render, redirect





def reg(request):
    if request.method == 'POST':
        obj = Userreg()
        obj.first_name=request.POST.get('first_name')
        obj.second_name=request.POST.get('second_name')
        obj.email=request.POST.get('email')
        obj.password=request.POST.get('password')

        obj.save()

        print(obj.first_name)
        print(obj.second_name)
        print(obj.email)
        print(obj.password)
        return redirect('ind')

    return render(request,'reg.html')

def dashboard(request):
    obj = Userreg.objects.all()

    data ={
        'x' : obj,
    }

    return render(request,'userview.html', data)

def dash(request):

    return render(request,'dashboard.html')

def cont(request):

    return render(request,'contact.html')
