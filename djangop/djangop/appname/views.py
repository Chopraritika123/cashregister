from typing import ContextManager
from django.shortcuts import render, HttpResponse
from .models import Hill

def home(request):
    data=Hill.objects.all()
    for i in data:
        print(i.id)
    ##context = {
        #"variable":"this is sent"
    #}
    if request.method == "POST":
        
        date= request.POST.get('date',"")
        time = request.POST.get('time',"")
        remarks=request.POST.get('remarks',"")
        amount=request.POST.get('amount',"")
        sign=request.POST.get('sign',"")
        dusk = Hill(date=date, time=time, remarks=remarks, amount=amount, sign=sign)
        dusk.save()
        return render(request, "appname/home.html",{"data":data})


        
    return render(request, "appname/home.html",{"data":data})
