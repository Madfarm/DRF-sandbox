from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .quickstart_walkthrough import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewset)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cats/', views.ListCreateCatAPIView.as_view(), name='get_post_cats'),
    path('cats/<int:pk>/', views.RetrieveUpdateDestroyCatAPIView.as_view(), name='get_delete_update_cat'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
