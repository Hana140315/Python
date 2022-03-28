from django.shortcuts import render, redirect

# Create your views here.
def result(request):
    if request.method =="GET":
        return  render(request,'index.html')

def showdata(request):
    if request.method == "POST":
        context= {
            "name_res":request.POST["name"],
            "Location_res": request.POST["Location"],
            "Language_res": request.POST["Language"],
            "Comment_res":request.POST["Comment"]
        }
    return render(request,"result.html" ,context)
               