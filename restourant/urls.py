from restourant.views import *
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

restaurant_list = RestaurantViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
restaurant_detail = RestaurantViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dish_list = RestaurantViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
dish_detail = RestaurantViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='restaurant-detail'),
    url(r'^restaurant/$', restaurant_list, name='snippet-list'),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', restaurant_detail, name='restaurant-detail'),
    url(r'^dish/$', dish_list, name='dish-list'),
    url(r'^dish/(?P<pk>[0-9]+)/$', dish_detail, name='dish-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])