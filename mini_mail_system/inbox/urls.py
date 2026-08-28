from django.urls import path

from . import views

urlpatterns = [
    # Kept at the app root (not "inbox/inbox/") since this gets
    # included under path('inbox/', ...) in the project's urls.py.
    path('', views.inbox_view, name='inbox'),
    path('sent/', views.sent_view, name='sent'),
    path('compose/', views.compose_view, name='compose'),
    path('<int:pk>/', views.message_detail, name='message_detail'),
]
