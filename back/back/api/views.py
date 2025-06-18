from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Apartments
from .serializers import ApartmentSerializer


class ApartmentView(APIView):
    def get(self, request):
        if ['id'] not in request.query_params :
            apartments = Apartments.objects.all()
            serializer = ApartmentSerializer(apartments, many=True)
            return Response(serializer.data)
        else :
            apartments = get_object_or_404(Apartments,pk=request.query_params['id'])
            serializer = ApartmentSerializer(apartments, many=False)
            return Response(serializer.data)

    def post(self, request):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request):
        apartments = get_object_or_404(Apartments,pk=request.query_params['id'])
        apartments.delete()
        return Response({'status:success'},status=200)