"""WebApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from WebApp.views import home,table,data_save,view_update_booking,view_update_form_data_in_db,delete_object
from uploadapp.views import index,normalupload


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/booking',home),
    path("web/table",table),
    path("web/save",data_save),
    path("web/edit/<int:ID>",view_update_booking),
    path("web/edit/update/<int:ID>",view_update_form_data_in_db),
    path('web/delete/<int:ID>',delete_object),
    path('',index),
    path('home/',index),
    path('normalupload',normalupload,name="noramalupload")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
