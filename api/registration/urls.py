from django.urls import path

from api.registration.views import AdminModeratorRegisterView, CompanyModeratorRegisterView, CompanyRegisterView, \
    AdminRegisterView, ResearcherRegisterView

urlpatterns = [
    path('researcher/', ResearcherRegisterView.as_view(), name='company_moderator_registration'),
    path('company/', CompanyRegisterView.as_view(), name='company_moderator_registration'),
    path('admin/', AdminRegisterView.as_view(), name='admin_moderator_registration'),
    path('admin_moderator/', AdminModeratorRegisterView.as_view(), name='admin_moderator_registration'),
    path('company_moderator/', CompanyModeratorRegisterView.as_view(), name='company_moderator_registration'),
]
