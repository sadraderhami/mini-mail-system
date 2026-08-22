from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Message


@login_required
def search_users(request):
    query = request.GET.get("q", "").strip()
    results = []
    if query:
        results = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
    return render(request, "search.html", {"query": query, "results": results})


@login_required
def chat(request, username):
    other_user = get_object_or_404(User, username=username)

    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            Message.objects.create(sender=request.user, receiver=other_user, text=text)
        return redirect("chat", username=username)

    thread = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) | Q(sender=other_user, receiver=request.user)
    )
    return render(request, "chat.html", {"other_user": other_user, "messages": thread})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("search")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
