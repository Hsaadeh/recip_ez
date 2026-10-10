from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.settings import DEFAULT_VIEW



@login_required(login_url="/sign-in")
def view_home(request):
    context = {
        "page_title": "Home",
    }

    return render(request, "home.html", context)


def view_sign_in(request):
    if request.user.is_authenticated:
        return redirect(DEFAULT_VIEW)
    
    context = {
        "page_title": "Sign in",
        "sign_in_page": True,
    }

    return render(request, "sign_in.html", context)


def view_not_found(request):
    context = {
        "page_title": "Page not found",
    }

    return render(request, "page_not_found.html", context)


@login_required(login_url="/sign-in")
def view_redirect(request):
    return redirect(DEFAULT_VIEW)
