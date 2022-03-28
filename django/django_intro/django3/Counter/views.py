from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if "count" not in request.session:
            request.session["count"] = 1
    else:
            request.session["count"] += 1
    return render(request,"index.html")


def counter(request):
    if request.POST['add_btn'] == 'add':
        print("I am in first if")
        pass
    elif request.POST['add_btn'] == 'rest':
        print("I am in el if")
        request.session["count"] = -1

    return redirect("/")

# def destroy(request):
#         return redirect("/")

