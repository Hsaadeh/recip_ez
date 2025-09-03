from django.shortcuts import render, redirect
from app.settings import DEFAULT_VIEW



def view_home(request):
    
    context = {
        "page_title": "Home",
    }

    return render(request, "home.html", context)


def view_not_found(request):
    
    context = {
        "page_title": "Page not found",
    }

    return render(request, "page_not_found.html", context)

def view_redirect(request):
    return redirect(DEFAULT_VIEW)
