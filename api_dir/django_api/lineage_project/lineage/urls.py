# lineage/urls.py

from django.urls import path
from .views import get_job_lineage

urlpatterns = [
    path('lineage/<str:job_name>/', get_job_lineage, name='get_job_lineage'),
]
