from django.shortcuts import render , HttpResponse
def index(request):
    # return HttpResponse("this is home page")
    peoples = [
        {"name":"rishu","age":25},
        {"name":"aman","age":29},
        {"name":"kuamr","age":21}
        
    ]
    for people in peoples:
        print(peoples)
        
    return render(request, 'index.html', context={'peoples'})

# def about(request):
#     return HttpResponse ("this is about page")
# def services(request):
#     return HttpResponse ("this is services page")
# def contact(request):
#     return HttpResponse ("this is contact page")

