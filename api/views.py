from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets, mixins
from rest_framework.filters import SearchFilter

from .models import Follow, Group, Post, User
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations with posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('group', )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for CRUD operations with comments
    """
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly
    )

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs.get('id'))
        )


class GroupViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    Viewset for viewing and creating groups
    """
    queryset = Group.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = GroupSerializer


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Viewset for viewing and creating groups
    """
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter, )
    search_fields = ('user__username', 'following__username', )

    def get_queryset(self):
        get_object_or_404(User, id=self.request.user.pk)
        return Follow.objects.filter(following=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
