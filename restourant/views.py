# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restourant.serializers import *
from restourant.models import Restouran, Dish
from rest_framework.decorators import detail_route
from restourant.permissions import IsOwnerOrReadOnly

from rest_framework import permissions, renderers
from rest_framework.reverse import reverse


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'dish': reverse('dish-list', request=request, format=format),
        'restourant':reverse('restourant-list', request=request, format=format),
        'comment': reverse('comment-list', request=request, format=format),
    })

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restouran.objects.all()
    serializer_class = RestouranSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)