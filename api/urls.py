from django.urls import path
from . import views

urlpatterns = [
    path('api/actions/', views.SustainabilityActionListCreateView.as_view(), name='action-view-create'),
    path('api/actions/<int:pk>/', views.SustainabilityActionRetrieveUpdateDestroyView.as_view(), name='update-delete-action'),
]