from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from listings.api import views as listings_api_views
from users.api import views as users_api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('api/listings/', listings_api_views.ListingList.as_view()),
    path('api/listings/create/', listings_api_views.ListingCreate.as_view()),
    path('api/listings/<int:pk>/', listings_api_views.ListingDetail.as_view()),
    path('api/listings/<int:pk>/delete/', listings_api_views.ListingDelete.as_view()),
    path('api/listings/<int:pk>/update/', listings_api_views.ListingUpdate.as_view()),
    
    
    path('api/profiles/', users_api_views.ProfileList.as_view()),
    path('api/profiles/<int:seller>/', users_api_views.ProfileDetail.as_view()),
    path('api/profiles/<int:seller>/update/', users_api_views.ProfileUpdate.as_view()),
    
    
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
