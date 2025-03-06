from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_page, about

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("user_page/", user_page, name="user_page"),
    path("about/", about, name="about"),
]
