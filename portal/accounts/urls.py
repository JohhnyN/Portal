from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    user_page,
    about,
    tasks,
    task_create,
    task_edit,
    task_delete,
    task_complete,
    task_detail,
    profile,
)

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path("user_page/", user_page, name="user_page"),
    path("about/", about, name="about"),
    path("tasks/", tasks, name="tasks"),
    path("tasks/create/", task_create, name="task_create"),
    path("tasks/<int:pk>/edit/", task_edit, name="task_edit"),
    path("tasks/<int:pk>/delete/", task_delete, name="task_delete"),
    path("tasks/<int:pk>/complete/", task_complete, name="task_complete"),
    path("tasks/<int:pk>/", task_detail, name="task_detail"),
    path("profile/", profile, name="profile"),
]
