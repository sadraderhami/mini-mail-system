from django.urls import path
from . import views

urlpatterns = [
    path("", views.search_users, name="search"),
    path("chat/<str:username>/", views.chat, name="chat"),
    path("accounts/signup/", views.signup, name="signup"),
]
