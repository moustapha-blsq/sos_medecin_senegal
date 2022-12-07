from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patient.urls')),
    #path('add_patient', include('patient.urls')),
   # path('get_patient', include('patient.urls')),
    path('', include('personnel.urls'))

]
