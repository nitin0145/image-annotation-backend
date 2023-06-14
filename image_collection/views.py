from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import base64
from .serializers import *
from bson.objectid import ObjectId

class Image_collectionViewSet(viewsets.ModelViewSet):
    serializer_class = Image_collectionSerializer
    queryset = Image_collection.objects.all()

    # create image collection with base64 image

    def create(self, request, *args, **kwargs):
        form_data = request.data

        imageBase64 = base64.b64encode(form_data['image'].read())
        finalBase64 = "data:image/png;base64," + imageBase64.decode('utf-8')
        form_data['imageBase64'] = finalBase64
        form_data['file_size'] = form_data['image'].size
        form_data['file_type'] = form_data['image'].content_type
        form_data['name'] = form_data['image'].name

        serializer = self.get_serializer(data=form_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# update key points of image collection
    
@api_view(['PUT'])
def update_key_points(request):
    try:
        id = request.data['id']
        image_collection = Image_collection.objects.get(
            _id=ObjectId(id))
        data = request.data
        image_collection.key_points = data['key_points']
        image_collection.save()

        serializer = Image_collectionSerializer(image_collection)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

