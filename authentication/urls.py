from django.contrib import admin
from django.urls import path
from authentication import views as auth_view
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
                path('support/auth/login',auth_view.SupportLoginView.as_view()),
                path("support/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path('patient/auth/login',auth_view.PatientLoginView.as_view()),
                path("patient/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path('admin/auth/login',auth_view.AdminLoginView.as_view()),
                path("admin/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                path('staff/auth/login',auth_view.StaffLoginView.as_view()),
                path("staff/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]