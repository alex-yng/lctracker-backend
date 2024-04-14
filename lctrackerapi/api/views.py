from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.
class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk' # primary key

@api_view(['POST'])
def MakeNote(request):
    if request.method == 'POST':
        print(request.data)
        Note.objects.create(title=request.data['title'], content=request.data['content'])
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Note.objects.all()
    
@api_view(['GET'])
def GetNotes():
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)