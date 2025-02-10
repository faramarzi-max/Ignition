from django.urls import path, include  # Importing path and include functions from django.urls
from rest_framework.routers import DefaultRouter  # Importing DefaultRouter from rest_framework.routers
from .views import RecordViewSet  # Importing RecordViewSet from the current package's views module


# Define the app name
app_name = 'records'

router = DefaultRouter()  # Creating an instance of DefaultRouter
router.register(r'records', RecordViewSet)  # Registering the RecordViewSet with the router under the URL prefix 'records'

urlpatterns = [
    path('', include(router.urls)),  # Including the router's URLs in the urlpatterns list
]
