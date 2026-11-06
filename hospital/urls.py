from django.contrib import admin
from django.urls import include, path
from hospital import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(),name='home'),
    path('patients/',include('employee.urls')),
    path('accounts/',include('accounts.urls')),
    
    #API endpoints:domainname/api/v1
    path('api/v1/',include('api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
