from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"editorials", views.EditorialViewSet),
router.register(r"personas", views.PersonaViewSet),
router.register(r"libros", views.LibroViewSet)


urlpatterns = [
    # path('', views.hello),
    #path('about/', views.about)
     path("", include(router.urls))
]