from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers 
from .import views


router = routers.DefaultRouter()
router.register('contents', views.ContentViewSet)
router.register('services', views.ServiceViewSet)
router.register('projects', views.ProjectViewSet)
router.register('team-members', views.TeamMemberViewSet)
router.register('careers', views.CareerViewSet)
router.register('images', views.ImageViewSet)
router.register('categorys', views.CategoryViewSet)

urlpatterns = router.urls 







# urlpatterns = [
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.jwt')),
# ]
