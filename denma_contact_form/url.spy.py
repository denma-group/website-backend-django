from django.urls import path, include
from rest_framework.routers import DefaultRouter
from denma_contact_form import views

router = DefaultRouter()
router.register('contact', views.ContactFormViewSet, base_name='contact')

urlpatterns = [
    path('', include(router.urls)),
]
