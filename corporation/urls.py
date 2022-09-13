from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('list', views.ListCorporation.as_view(), name='list'),
    path('retrieve/:id', views.ListCorporation.as_view(), name='retrieve')
]

router = DefaultRouter()
router.register('', views.CorporationViewSet, basename='corporations')
urlpatterns.extend(router.urls)