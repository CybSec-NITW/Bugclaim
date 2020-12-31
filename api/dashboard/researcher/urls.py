from django.urls import path

from api.dashboard.researcher.views import ResearcherView

urlpatterns = [
    path('researcherprofile/', ResearcherView.as_view()),
]
