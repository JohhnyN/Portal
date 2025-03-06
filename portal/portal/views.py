from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, "main/404.html", status=404)


def page_not_found_view2(request, exception):
    return render(request, "main/403.html", status=403)
