from .models import Notification

from django.contrib.auth.decorators import login_required

@login_required()
def list_unread_notifications(request):
    unread_notifications = Notification.objects.filter(user = request.user , unread = False).count()
    return {'unread_notifications':unread_notifications}