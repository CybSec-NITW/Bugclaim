from django.urls import path

from api.dashboard.root.views import RootAdminView, RootModView

urlpatterns = [
    path('rootadminprofile/', RootAdminView.as_view()),
    path('rootmodprofile/', RootModView.as_view()),
]
