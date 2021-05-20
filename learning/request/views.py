from django.shortcuts import render



def request(request):

    print(request.COOKIES)




    context={'hi':'hello world'}

    return render(request,'request/index.html',context)