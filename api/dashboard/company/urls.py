from django.urls import path

from api.dashboard.company.views import CompanyAdminView, CompanyModView

urlpatterns = [
    path('companyadminprofile/', CompanyAdminView.as_view()),
    path('companyModprofile/', CompanyModView.as_view()),
]
