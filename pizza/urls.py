"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("orders.urls")),
    path("", include("carts.urls")),
    path("", include("products.urls")),
]
# urlpatterns += i18n_patterns(
#     path("", include("accounts.urls")),
#     prefix_default_language=False,
# )
# urlpatterns += i18n_patterns(
#     path("", include("orders.urls")),
#     prefix_default_language=False,
# )
# urlpatterns += i18n_patterns(
#     path("", include("carts.urls")),
#     prefix_default_language=False,
# )
# urlpatterns += i18n_patterns(
#     path("", include("products.urls")),
#     prefix_default_language=False,
# )