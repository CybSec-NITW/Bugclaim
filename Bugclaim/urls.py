"""Bugclaim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers
from rest_auth.registration.views import VerifyEmailView, RegisterView

router = routers.DefaultRouter()

urlpatterns = [
                  path('logout', LogoutView.as_view(), name='user-logout'),
                  path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
                  path('password/reset', PasswordResetView.as_view(), name='rest_password_reset'),
                  path('password/reset/confirm/', PasswordResetConfirmView.as_view(),
                       name='rest_password_reset_confirm'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('admin/', admin.site.urls),
                  path('dashboard/', include('api.dashboard.urls')),
                  path('api/', include('api.urls')),
                  path('docs/', include_docs_urls(title='BugClaim API Documentation')),
                  path('register/', include('api.registration.urls')),
                  re_path('account-confirm-email/', VerifyEmailView.as_view(),
                          name='account_email_verification_sent'),
                  re_path('account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
                          name='account_confirm_email'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
