from .models import Message


def unread_count(request):
    # Runs on every template render (registered in settings.py), so the
    # navbar badge works everywhere without each view passing this in.
    if not request.user.is_authenticated:
        return {}
    count = Message.objects.filter(recipient=request.user, is_read=False).count()
    return {'unread_count': count}
