from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from gtts import gTTS
from .models import Audio
from .serializers import AudioSerializer
import os

class AudioCreateView(generics.CreateAPIView):
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Audio file created successfully',
            'id': serializer.data['id'],
            'audio_file': serializer.data['audio_file'],
        }, status=status.HTTP_201_CREATED, headers=headers)
    
