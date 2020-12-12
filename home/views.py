from django.shortcuts import render ,HttpResponse

# Create your views here.
class action:
    
    def index(self, request):
        #return HttpResponse("this is home page")
        context={
        'variable':"Prince"
        }
        return render(request,"index.html")

    def about(self,request):
            a=request.POST
            print(a)
       #return HttpResponse("this is home about page")
            return render(request,"about.html")
    
    #return render(request,"index.html")

    def services(self,request):
       #return HttpResponse("this is services page")
       return render(request,'services.html')
   
    
    #return render(request,"index.html")
    def contact(self,request):
        #return HttpResponse("this is contact page")
         return render(request, "contact.html")
    #return render(request,"index.html")
    