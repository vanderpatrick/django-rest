from rest_framework import generics, permissions
from drf_api.permission import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentSerializerDetail
from django_filters.rest_framework import DjangoFilterBackend



class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        "post"
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializerDetail
    queryset = Comment.objects.all()
