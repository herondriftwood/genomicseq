from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sequence.models import Sequence
from sequence.serializers import SequenceSerializer


class SequenceView(APIView):

    def get(self, request):
        patients = Sequence.objects.all()
        serializer = SequenceSerializer(patients, many=True)
        response_data = {'sequences': serializer.data}
        return JsonResponse(response_data, safe=False)

    def post(self, request):
        serializer = SequenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
