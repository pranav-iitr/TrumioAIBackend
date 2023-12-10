
from django.contrib import admin
from django.urls import path,include
import gpt.urls as gpt_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(gpt_urls)),

]
