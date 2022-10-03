from django.shortcuts import render, redirect
from .models import Links

def index(request):
    links = Links.objects.all()
    if request.method == 'POST':
        if request.POST.get("remove") == None:
            title = str(request.POST.get("txtTitle"))
            url = str(request.POST.get("txtUrl"))
            new_url = Links(title=title , url=url)
            new_url.save()
        else:
            Links.objects.all().delete()
        return redirect("index")
    return render(request , 'links/index.html' , {'links':links})