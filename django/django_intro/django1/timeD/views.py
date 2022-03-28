from multiprocessing import context
from django.shortcuts import render 
from datetime import datetime

# Create your views here.
def display_time(request):
    now=datetime.today()
    context={"date": now.strftime('%b %d, %Y'),
"time": now.strftime('%H: %M %p')}
    return render(request, 'index.html', context)
            