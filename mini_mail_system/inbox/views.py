from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MessageForm
from .models import Message


@login_required
def inbox_view(request):
    # Note the context key is `received_messages`, not `messages` —
    # `messages` is already used by django.contrib.messages for flash
    # banners ("Login successful", etc.), so reusing it would silently
    # hide those on this page.
    received_messages = Message.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'inbox/inbox_list.html', {'received_messages': received_messages})


@login_required
def sent_view(request):
    sent_messages = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'inbox/sent_list.html', {'sent_messages': sent_messages})


@login_required
def compose_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # commit=False builds the Message in memory without saving,
            # so we can fill in `sender` (not on the form) before it hits the DB.
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('sent')
    else:
        form = MessageForm()
    return render(request, 'inbox/compose.html', {'form': form})


@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    # Only the two people involved should be able to open this message —
    # without this check, anyone logged in could read anyone else's mail
    # just by guessing/incrementing the URL's id.
    if request.user not in (message.sender, message.recipient):
        return redirect('inbox')
    if request.user == message.recipient and not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'inbox/message_detail.html', {'message': message})
