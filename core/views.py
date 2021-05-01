from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    try:
        if request.method=='POST':
            f = request.POST.get('fname',False)
            s = request.POST.get('sname',False)
            res = calculator(f,s)
            context ={
            'fname':res['fname'],
            'sname':res['sname'],
            'percent':int(res['percentage']),
            'result':res['result'],
            }
            return render(request,'core/result.html',context={'data':context})
        return render(request,'core/home.html')
    except:
        return render(request,'core/error.html')
    
# def test(request):
#     return render(request,'core/error.html')

def calculator(f,s):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"fname":f"{f}","sname":f"{s}"}

    headers = {
        'x-rapidapi-key': "Your Rapid API Key",
        'x-rapidapi-host': "love-calculator.p.rapidapi.com"}

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return response
