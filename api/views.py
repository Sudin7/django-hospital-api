from rest_framework.views import APIView
from rest_framework.response import Response
from employee.models import Staff, Type ,Patient
from .serializers import StaffSerializer, TypeSerializer,PatientSerializer
from rest_framework import status

#Api view is for CBV (@api_view(['GET', 'POST']))


class TypeView(APIView):

    def get(self, request):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TypeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class StaffView(APIView):

    def get(self, request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientView(APIView):

    def get(self, request):
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     