from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
from bqsang import views
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
   path('', views.home_view, name='home'),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
