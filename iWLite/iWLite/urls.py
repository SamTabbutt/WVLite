from django.contrib import admin
from django.urls import path, include, re_path
from identify import views as v
import rest_framework.routers as routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'animals', v.AnimalViewList)
router.register(r'capture', v.CaptureViewList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('predict/', v.ImagePredictView.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)