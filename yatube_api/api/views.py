"""Views для API Yatube."""

from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)


class OptionalLimitOffsetPagination(LimitOffsetPagination):
    """Пагинация только при наличии limit/offset в запросе."""

    def paginate_queryset(self, queryset, request, view=None):
        if 'limit' not in request.query_params and 'offset' not in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с публикациями."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = OptionalLimitOffsetPagination

    def perform_create(self, serializer):
        """Сохранение автора публикации."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для работы с сообществами (только чтение)."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с комментариями."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Получение комментариев к конкретной публикации."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """Сохранение автора комментария и публикации."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """ViewSet для работы с подписками."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        """Получение подписок текущего пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Сохранение подписки."""
        serializer.save(user=self.request.user)
