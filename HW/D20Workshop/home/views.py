from django.shortcuts import render, HttpResponse
import random

# Create your views here.

def index(request):
    return HttpResponse("welcome to Django")
    
def info(request):
    
    return render(request,'info.html')

def student(request,name):
    data = {'조성원':19, '둘리':49, '토마토':20, 'SM':18, 'HJ':15}
    #result = random.choice(data)
    #print(result)
    stu_age = data[name]
    return render(request,'student.html',{'stu_age':stu_age, 'name':name})
