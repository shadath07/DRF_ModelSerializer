from django.urls import path
from . import views


urlpatterns = [
    path('studentapi/',views.StudentAPI.as_view(), name = 'studentapi'),
]