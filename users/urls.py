from django.contrib import admin
from django.urls import path
from users import views as user_view



urlpatterns = [
                path('users',user_view.UserDetailListView.as_view()),
]