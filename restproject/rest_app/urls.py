from rest_framework import routers
from .views import Userviewset
from django.urls import path, include

from .views import UserListCreateView,UserRetrieveUpdateDestroyAPIView


router = routers.DefaultRouter()
router.register(r'User',Userviewset)

# urlpatterns = router.urls
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gen/', UserListCreateView.as_view(), name='item-list-create'),
    path('gen/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='item-retrieve-update-destroy'),

]
