"""
URL configuration for ignition_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views  # Import views from your app
    2. Add a URL to urlpatterns:  path('', views.home, name='home')  # Map URL to view function
Class-based views
    1. Add an import:  from other_app.views import Home  # Import class-based view
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')  # Map URL to class-based view
Including another URLconf
    1. Import the include() function: from django.urls import include, path  # Import include function
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))  # Include another URLconf
"""
from django.contrib import admin  # Import the admin module
from django.urls import path, include  # Import path and include functions for URL routing
from drf_yasg.views import get_schema_view  # Import get_schema_view for Swagger documentation
from drf_yasg import openapi  # Import openapi for Swagger documentation
from rest_framework import permissions  # Import permissions for API access control

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the admin interface
    path('api/', include('records.urls', namespace='records')),  # Include URLs from the records app
]

# Configure the schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Ignition API",  # Title of the API
        default_version='v1',  # API version
        description="API for managing Ignition input/output data",  # Description of the API
    ),
    public=True,  # Make the documentation public
    permission_classes=(permissions.AllowAny,),  # Allow any permissions to access the documentation
)

# Add the Swagger UI URL pattern to the urlpatterns
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Route for Swagger UI
]
