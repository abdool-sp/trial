from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Data
from . import utils



@csrf_exempt
def home(request):
    r   =   'done'
    if request.method == 'POST':
        print(request.POST)
        payload = request.POST
        if 'user' in payload:
            user = payload.get('user')
            password = payload.get('pwd')
            #authenticate
            user_exist  =   User.objects.filter(username=user)
            if user_exist:
                if 'bpm' in payload and 'temp' in payload:
                    bpm     =   payload.get('bpm')
                    temp    =   payload.get('temp')
                    act_user                =   user_exist.first()
                    new_data                =   Data()
                    new_data.User           =   act_user
                    new_data.heart_rate     =   int(bpm)
                    new_data.temperature    =  int(temp)
                    new_data.save()
                return HttpResponse('User exist')
            else:
                HttpResponse('User does not exist')
            return HttpResponse('User does not exist')

    return HttpResponse(r)

def home2(request):
    context = {
        'data': Data.objects.all()

    }
    return render(request,template_name='home.html',context=context)