from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('image_location/<location>/',views.image_by_location,name='image_by_location'),
    path('search/',views.search_by_category,name="search"),
    path('image/<int:image_id>/',views.single_image,name='image')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    