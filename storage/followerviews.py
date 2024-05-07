from rest_framework import generics, permissions
from api_practice.permissions import IsOwnerOrReadOnly
from follower.model import Follower
from follower.serializer import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    permissions_class = [IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Followers.Objects.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)
    
class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_class =[IsAuthenticatedOrReadOnly]
    serializer_class =FollowerSerializer
    querset = Follower.objects.all()