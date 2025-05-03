# lineage_project/urls.py

from django.contrib import admin
from django.urls import path, include  # include() is necessary to include other apps' urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('lineage.urls')),  # This includes the urls.py from the 'lineage' app
]
