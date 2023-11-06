from django.urls import include, path
from . import views

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions, authentication

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'user', views.CustomUserViewSet)
router.register(r'model3d', views.Model3dViewSet)
router.register(r'badge', views.BadgeViewSet)
# router.register(r'actions',views.UserBadgesView,basename='custom')


 

schema_view = get_schema_view(
   openapi.Info(
      title="CodeLN TEST API",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="kouameulrich45@gmail.com"),
      license=openapi.License(name="KOUAME MOAYE ULRICH (kouameulrich45@gmail.com)"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
   authentication_classes = (authentication.SessionAuthentication,)
)

urlpatterns = [
    
    

    path(r'models/', include(router.urls)),
    path('docs/', include_docs_urls(title='Your API')),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # # Endpoint for uploading 3D models
    # path('action/user/<int:user_id>/upload/', views.upload_model, name='upload_model'),

    # Endpoint for fetching a user's badges
    path('action/user/<int:user_id>/badges/', views.user_badges, name='user_badges'),

    # Endpoint for awarding the 'Star' badge
    path('action/user/<int:user_id>/model/<int:model_id>/star-badge/', views.star_badge, name='star_badge'),

    # Endpoint for awarding the 'Collector' badge
    path('action/user/<int:user_id>/collector-badge/', views.collector_badge, name='collector_badge'),

    # Endpoint for awarding the 'Pioneer' badge
    path('action/user/<int:user_id>/pioneer-badge/', views.pioneer_badge, name='pioneer_badge'),

]
