from django.urls import re_path
from . import views  # add
from django.conf import settings # add
from django.conf.urls.static import static # add

urlpatterns = [
    re_path(r'^$', views.first_view, name='first_view'),
    re_path(r'^uimage/$', views.uimage, name='uimage'), # add
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)