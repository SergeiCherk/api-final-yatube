"""Права доступа для API Yatube."""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение на изменение только для автора объекта.

    Остальным пользователям доступно только чтение.
    """

    def has_object_permission(self, request, view, obj):
        """Проверка прав доступа к объекту."""
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Изменение разрешено только автору
        return obj.author == request.user
