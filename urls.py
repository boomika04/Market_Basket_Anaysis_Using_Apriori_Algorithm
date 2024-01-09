from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('veg.html', views.veg, name='veg'),
    path('fruits.html', views.fruits, name='fruits'),
    path('cold.html', views.cold, name='cold'),
    path('dairy.html', views.dairy, name='dairy'),
    path('dry.html', views.dry, name='dry'),
    path('addtocart.html', views.addtocart, name='addtocart'),
    path('about.html', views.about, name='about'),
    path('spi.html', views.spi, name='spi'),
    path('login.html', views.login, name='login'),
    path('product/<str:item_name>/', views.product, name='product') # Corrected URL pattern
    # Add other URL patterns as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
