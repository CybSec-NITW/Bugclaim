from django.urls import path

from api.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='my_custom_login'),
]
