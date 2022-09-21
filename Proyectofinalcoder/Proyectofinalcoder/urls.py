<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("AppFut/", include("AppFut.urls")),
=======
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("AppFut/", include("AppFut.urls")),
>>>>>>> 6c7c70af40c3c22414841de5994e786f2607dce8
]