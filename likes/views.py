from rest_framework import generics, permissions
from api_practice.permissions import IsOwnerOrReadOnly
from .models import Likes
from .serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    permission_class =[permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    querset = Likes.objects.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_class =[permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    querset = Likes.objects.all()
