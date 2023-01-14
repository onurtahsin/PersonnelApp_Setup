from rest_framework import serializers
from .models import Department,Personnel

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        personnel_count = serializers.SerializerMethodField()
        model = Department
        fields = ("id","name","personnel_count")
        
        def get_personel_count(self,obj):
            return obj.personals.count()