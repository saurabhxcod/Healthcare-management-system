from django.urls import path
from .views import MappingListCreateView, MappingDetailOrPatientDoctorsView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:id_param>/', MappingDetailOrPatientDoctorsView.as_view(), name='mapping-detail-or-patient'),
]
