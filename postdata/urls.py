from django.urls import path
from . import views
urlpatterns = [
    path('', views.overAPIView, name='over-apiview'),
    path('raw-data', views.ResponesData, name='respone-data'),
]
