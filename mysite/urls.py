from django.contrib import admin
from django.urls import path
from myapp import views as appview

urlpatterns = [
    path('', appview.index),
    path('index', appview.index),
    path('dev', appview.dev),
    path('admin/', admin.site.urls),
]
