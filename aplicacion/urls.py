from rest_framework import routers
from .views import ViewsetAplicacion

router = routers.DefaultRouter()

router.register('api/aplicacion' , ViewsetAplicacion, 'aplicacion')

urlpatterns = router.urls