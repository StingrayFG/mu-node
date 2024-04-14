from django.urls import path
from rest_framework import routers

from quickstart import views


router = routers.SimpleRouter()
router.register(r'folder', views.FolderView)

urlpatterns = [
    path('folder/get/uuid/<uuid>/', views.FolderView.get_by_uuid)
]

urlpatterns = [
    path('file/download/<uuid>/', views.FileView.get_download_link)
]