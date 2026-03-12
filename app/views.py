from django.shortcuts import render

from .models import Media
def landing(req):
    if req.method == "POST":
        i= req.FILES.get('image')
        a= req.FILES.get('audio')
        v= req.FILES.get('video')
        Media.objects.create(Image=i,Audio=a,Video=v)
    return render(req,'landing.html')

def all_data(req):
    alldata = Media.objects.all()
    return render(req,'landing.html',{'all_data':alldata})
    