from django.urls import path
from . import views

urlpatterns = [
    path('face/', views.UploadFace),
    path('delete/', views.DeleteFace),
]