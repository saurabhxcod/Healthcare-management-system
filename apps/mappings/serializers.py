from rest_framework import serializers
from .models import PatientDoctorMapping
from apps.patients.serializers import PatientSerializer
from apps.doctors.serializers import DoctorSerializer
from apps.patients.models import Patient
from apps.doctors.models import Doctor

class MappingSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source='patient', write_only=True
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), source='doctor', write_only=True
    )

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient_id', 'doctor_id', 'assigned_at']

    def validate(self, data):
        patient = data.get('patient')
        doctor = data.get('doctor')
        request = self.context.get('request')

        if request and patient.created_by != request.user:
            raise serializers.ValidationError("You do not have permission to map this patient.")
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This doctor is already assigned to this patient.")

        return data

class MappingReadSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_at']
