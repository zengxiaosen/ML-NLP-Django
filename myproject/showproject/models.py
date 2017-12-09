# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url,include
from django.contrib import admin
from django.db import models
from django.conf import settings
from django.conf.urls.static import static

# Create your models here.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^showproject/', include('showproject.urls', namespace='showproject')),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)