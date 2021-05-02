from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, rssFeed, GenericAPIView, ModelRouterviewset, RouterViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ModelRouterviewset, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('genericAllrticle/', GenericAPIView.as_view() ),
    path('genericarticle/<int:id>/', GenericAPIView.as_view() ),
    path('article/', ArticleAPIView.as_view() ),
    path('rssfeed/', rssFeed.as_view() )
]
