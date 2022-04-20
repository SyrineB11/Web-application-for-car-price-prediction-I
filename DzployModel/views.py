from django.http import HttpResponse
from django.shortcuts import render
import joblib
import numpy as np
def home(request):
    return render(request,'home.html')
def result(request):
    model= joblib.load('finalized.sav')
    list=[]
    list.append(request.GET['a'])
    list.append(request.GET['b'])
    list.append(request.GET['c'])
    list.append(request.GET['d'])
    list.append(request.GET['e'])
    list.append(request.GET['f'])
    list.append(request.GET['g'])
    print(list)
    ans=model.predict(np.array(list).reshape(1,-1))
    H=ans[0]
    return render(request,"result.html",{'ans':H})