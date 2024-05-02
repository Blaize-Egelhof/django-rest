from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api_practice.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer , CommentDetailSerializer

#The following view is a generic view , created to skip over repetitive GET and POST Views , refer to POST views as its basically the same concept.

#This view generates an API view with full CRUD 

class CommentList(generics.ListCreateAPIView):  #In the Name after generics. List is responsible for Get Requests , uses 'create'
    filter_backends =[

        DjangoFilterBackend
    ]

    filterset_fields = ['post']

    serializer_class = CommentSerializer
    permissions_class =[permissions.IsAuthenticatedOrReadOnly ]
    queryset = Comment.objects.all()

    def perform_create(self, serializer): # This class creates a comment automatically according to the data given above
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()

