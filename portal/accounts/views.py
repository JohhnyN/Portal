from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task, CustomUser
from .forms import TaskForm, CommentForm, ProfileUpdateForm


@login_required
def user_page(request):
    return render(request, "accounts/user_page.html", {"user": request.user})


@login_required
def about(request):
    return render(request, "accounts/about.html")


@login_required
def tasks(request):
    query = request.GET.get("q")
    if query:
        user_tasks = Task.objects.filter(
            user=request.user, title__icontains=query
        ) | Task.objects.filter(shared_with=request.user, title__icontains=query)
    else:
        user_tasks = Task.objects.filter(user=request.user) | Task.objects.filter(
            shared_with=request.user
        )

    user_tasks = user_tasks.distinct().order_by("is_completed", "-created_at")

    tasks_with_comments = []
    for task in user_tasks:
        shared_with_comments = []
        for user in task.shared_with.all():
            shared_with_comments.append(
                {"user": user, "has_comments": task.has_comments_from_user(user)}
            )
        tasks_with_comments.append(
            {"task": task, "shared_with_comments": shared_with_comments}
        )
    return render(
        request,
        "accounts/tasks.html",
        {
            "tasks_with_comments": tasks_with_comments,
            "CURRENT_LANGUAGE": request.LANGUAGE_CODE,
        },
    )


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            form.save_m2m()
            return redirect("tasks")
    else:
        form = TaskForm(user=request.user)
    return render(request, "accounts/task_form.html", {"form": form})


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("tasks")
    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, "accounts/task_form.html", {"form": form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    return render(request, "accounts/task_confirm_delete.html", {"task": task})


@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.completed_at = timezone.now()
    task.save()
    return redirect("tasks")


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.comments.all()
    if request.method == "POST":
        print("POST запрос получен")
        form = CommentForm(request.POST)
        if form.is_valid():
            print("Форма валидна")
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            print("Комментарий сохранен")
            return redirect("task_detail", pk=task.pk)
    else:
        form = CommentForm()
        print(form.errors)
    return render(
        request,
        "accounts/task_detail.html",
        {"task": task, "comments": comments, "form": form},
    )


@login_required
def profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})


@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "accounts/profile.html", {"form": form})


@login_required
def users(request):
    users = CustomUser.objects.filter(is_superuser=False)
    return render(request, "accounts/users.html", {"users": users})
