from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('searchbar.urls', namespace = 'searchbar')),
    path('accounts/', include('accounts.urls', namespace= 'accounts'))
]
