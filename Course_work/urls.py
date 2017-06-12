from django.conf.urls import url, include
from restourant import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.contrib import admin

schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'restaurant', views.RestaurantViewSet)
router.register(r'dish', views.DishViewSet)
router.register(r'comment', views.CommentViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]