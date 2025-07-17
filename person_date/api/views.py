from .serializer import PersonDateSerialiser
from ..models import PersonDate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


class PersonDateGetOrPost(APIView):

    def get(self,request):
        queryset=PersonDate.objects.all()
        serializer=PersonDateSerialiser(queryset,many=True)
        if queryset.exists():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"message": "Keine Person-Daten gefunden."},status=status.HTTP_404_NOT_FOUND)
    
    def post(self,request):
        serializer=PersonDateSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=PersonDate.objects.all()
    serializer_class = PersonDateSerialiser
