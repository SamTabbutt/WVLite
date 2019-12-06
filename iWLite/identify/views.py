from django.shortcuts import render
from rest_framework import viewsets, views, status
from .models import Animal, Capture
from .serializers import AnimalSerializer, CaptureSerializer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser
from PIL import Image
import numpy
from .datalearn import model

class AnimalViewList(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class CaptureViewList(viewsets.ModelViewSet):
    queryset = Capture.objects.all()
    serializer_class = CaptureSerializer


class ImagePredictView(views.APIView):
    parser_classes=[JSONParser, MultiPartParser]

    def post(self, request, format=None):
        file_obj = request.data['file']
        print(file_obj)
        im = Image.open(file_obj)
        nmp_im = numpy.array(im)
        print(nmp_im)
        (animal,confidence) = model.predict(nmp_im)

        return Response({'animal':animal,'confidence':confidence})
    
#class TrainImageModel(views.APIView):

#class PredictAnimal(views.APIView):