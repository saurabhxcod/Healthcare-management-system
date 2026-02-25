from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import MappingSerializer, MappingReadSerializer
from apps.patients.models import Patient

class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient__created_by=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MappingSerializer
        return MappingReadSerializer

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class MappingDetailOrPatientDoctorsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id_param):
        mappings = PatientDoctorMapping.objects.filter(
            patient_id=id_param, 
            patient__created_by=request.user
        )
        serializer = MappingReadSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, id_param):
        mapping = get_object_or_404(
            PatientDoctorMapping, 
            id=id_param, 
            patient__created_by=request.user
        )
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
