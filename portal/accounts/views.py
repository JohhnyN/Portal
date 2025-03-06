from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_page(request):
    return render(request, "accounts/user_page.html")


@login_required
def about(request):
    return render(request, "accounts/about.html")
