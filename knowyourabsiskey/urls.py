"""knowyourabsiskey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from knowyourabsiskey.settings import MEDIA_ROOT, MEDIA_URL
import whoisgame.views as wv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wv.index, name="index"),
    path('easy/', wv.easy, name="easy"),
    path('statistic/spawn/', wv.statistic_spawn, name="statistic_spawn"),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
