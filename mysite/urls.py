from django.contrib import admin
from django.urls import path
from myapp import views as appview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appview.test),
    path('index' , appview.index),
    path('test' , appview.test),
]
