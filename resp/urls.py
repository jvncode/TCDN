from django.urls import path
from resp.views import ResponseView

urlpatterns = [
    path('', ResponseView.as_view(), name='home'),
]