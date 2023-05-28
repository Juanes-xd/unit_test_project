from django.urls import re_path as url

from .views import *
# from . import views

app_name = "courses"

urlpatterns = [
    url(r'^$', course_list, name="list"),
    url(r'^(?P<pk>\d+)$', course_detail, name="detail"),
    url(r'^nuevo$', CourseCreation.as_view(), name="new"),
    url(r'^editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name="edit"),
    url(r'^borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name="delete"),

]
