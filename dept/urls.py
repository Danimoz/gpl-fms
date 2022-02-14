from django.urls import path
from .views import (FolderCreateView,)
from . import views

urlpatterns = [
    path('', views.FolderList, name='home'),
    path('folder/new/', FolderCreateView.as_view(), name='folder-create'),
    path('file/new/<int:pk>/', views.FileUploadForm, name='file-create'),
    path('folder/view/<int:pk>/', views.folderfiles, name='file-view'),
]