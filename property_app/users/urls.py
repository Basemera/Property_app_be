from django.urls import path
from .views import UserApiListView

urlpatterns = [
    path('register/', UserApiListView.as_view())
]