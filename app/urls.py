
from django.urls import path,include
from .views import StuidentViewset
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('get_student', StuidentViewset)



urlpatterns = [
    # path('', index, name='index'),
    path('',include(router.urls))
]