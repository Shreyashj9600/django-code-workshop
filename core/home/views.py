from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {'name':"abhijeet gupta" , "age": 26},
        {'name':"Rohan sharma" , "age":13},
        {'name':"viky kusha" , "age":24},
        {'name':"sandip" , "age":63}
    ]

    vegetable = ['pumpkin', 'tomato', 'potato']

    return render(request , 'index.html', context={'peoples' : peoples, 'vegetable':vegetable})


def about(request): 
    context = {'page':"About"}
    return render(request, "about.html", context)

def contact(request):   
    context = {'page':"Contact"} 
    return render(request, 'contact.html', context)


def success_page(request):
    return HttpResponse("<h1>this is a success page </h1>")