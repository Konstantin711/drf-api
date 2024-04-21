from django.contrib import admin
from django.urls import path
from django.urls import include


# http://localhost:8000/admin/


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]
