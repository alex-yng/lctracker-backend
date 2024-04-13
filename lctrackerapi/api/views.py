from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
# create a view that lists (using restframework) all note objects using the note serializer
class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'pk' # primary key