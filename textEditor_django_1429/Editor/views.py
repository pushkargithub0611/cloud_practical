from django.shortcuts import render
from .forms import TextForm

# Create your views here.

def index(request):
    if request.method=='POST':
        form=TextForm(request.POST)
        if form.is_valid():
            form.save()
    form=TextForm()
    return render(request,'index.html',{'form':form})
