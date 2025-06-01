from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import index, person, LoginAPI, PersonAPI, PeopleViewSet, RegisterAPI

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),      # POST http://127.0.0.1:8000/api/register/
    path('login/', LoginAPI.as_view(), name='login'),                # POST http://127.0.0.1:8000/api/login/
    path('', include(router.urls)),                                  # http://127.0.0.1:8000/api/people/  (ViewSet)
    path('index/', index, name='index'),                             # GET http://127.0.0.1:8000/api/index/
    path('person/', person, name='person_function_based'),           # GET/POST/etc. http://127.0.0.1:8000/api/person/
    path('persons/', PersonAPI.as_view(), name='person_class_based'), # GET/POST/etc. http://127.0.0.1:8000/api/persons/
    path('person-api/', PersonAPI.as_view(), name='person_api'),      # Same as above, for /api/person-api/
]
