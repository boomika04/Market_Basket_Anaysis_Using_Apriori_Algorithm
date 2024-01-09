from django.contrib import admin
from django.urls import path, include
from myapp import views  # Import the views module from your app

urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),

]
