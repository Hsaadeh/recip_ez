from django.shortcuts import render



def view_home(request):
    
    context = {
        "page_title": "Home",
    }

    return render(request, "home.html", context)
