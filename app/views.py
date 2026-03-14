from django.shortcuts import render,redirect

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
    

def edit(req,pk):
    edit_data = Media.objects.get(id=pk)
    if req.method == "POST":
        i= req.FILES.get('image')
        a= req.FILES.get('audio')
        v= req.FILES.get('video')
        edit_data.Image=i
        edit_data.Audio=a
        edit_data.Video=v
        edit_data.save()
        return redirect('all_data')
    return render(req,'landing.html',{'edit_data': edit_data})


def delete(req,pk):
    data = Media.objects.get(id=pk)
    data.delete()
    return redirect('all_data')