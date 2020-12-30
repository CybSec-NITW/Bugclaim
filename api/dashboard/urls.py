from django.urls import path

from .users import views as user_profile_views

urlpatterns = [
    path('rootadminprofile/', user_profile_views.RootAdminView.as_view()),
    path('rootmodprofile/', user_profile_views.RootModView.as_view()),
    path('companyadminprofile/', user_profile_views.CompanyAdminView.as_view()),
    path('companyModprofile/', user_profile_views.CompanyModView.as_view()),
    path('researcherprofile/', user_profile_views.ResearcherView.as_view()),
]
