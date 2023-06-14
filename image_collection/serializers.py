from rest_framework import serializers
from .models import *


class Image_collectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_collection
        fields = '__all__'

    def validate(self, data):
        file_type = data['file_type']
        if file_type not in ['image/jpeg', 'image/png']:
            raise serializers.ValidationError(
                {"error": "File type not supported"})
        elif data['file_size'] > 5000000:
            raise serializers.ValidationError(
                {"error": "File size too large"})
        return data
