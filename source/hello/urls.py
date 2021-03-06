"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from api.views import add_api, divide_api, subtract_api, multiply_api, api_view
from api_v2.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('webapp.urls')),
    path('add/', add_api, name='add'),
    path('subtract/', subtract_api, name='subtract'),
    path('multiply/', multiply_api, name='multiply'),
    path('divide/', divide_api, name='divide'),
    path('api/', api_view, name='api'),


    path('api-auth/', include('rest_framework.urls')),
    path('articlelist/', ArticleListView.as_view(), name='articlelist'),
    path('articlelist/<int:pk>', ArticleDetailView.as_view(), name='articledetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)