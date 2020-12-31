from django.urls import path, include

urlpatterns = [
    path('root/', include('api.dashboard.root.urls')),
    path('company/', include('api.dashboard.company.urls')),
    path('researcher/', include('api.dashboard.researcher.urls')),
]
