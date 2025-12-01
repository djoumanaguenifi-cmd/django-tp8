from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet, StudentCourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', StudentCourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]