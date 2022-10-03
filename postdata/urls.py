from django.urls import path
from . import views
urlpatterns = [
    path('', views.overAPIView, name='over-apiview'),
    path('post', views.ResponesData, name='respone-data'),
]
