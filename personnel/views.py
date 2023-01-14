from .models import Department, Personnel
from .serializers import DepartmentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes=[IsAuthenticated]