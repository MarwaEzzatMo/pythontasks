from rest_framework import serializers
from .models import Student , Track

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def to_representation(self , instance):
        temp = super().to_representation(instance)
        temp['student_track'] = instance.student_track.track_name
        return temp


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


