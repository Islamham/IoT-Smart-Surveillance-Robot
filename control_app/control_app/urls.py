from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #when the url has no extention, run views.home
    path("turn_left", views.turn_left), #when the url of the page get the /turn_left extention, run views.turn_left
    path("turn_right", views.turn_right), #when the url of the page get the /turn_right extention, run views.turn_right
    path("drive_forward", views.drive_forward), #when the url of the page get the /drive_forward extention, run views.drive_forward
    path("drive_backward", views.drive_backward), #when the url of the page get the /drive_backward extention, run views.drive_backward
    path("drive_stop", views.drive_stop), #when the url of the page get the /drive_stop extention, run views.drive_stop
    path("tilt_up", views.tilt_up), #when the url of the page get the /tilt_up extention, run views.tilt_up
    path("tilt_down", views.tilt_down), #when the url of the page get the /tilt_down extention, run views.tilt_down
    path("pan_left", views.pan_left), #when the url of the page get the /pan_left extention, run views.pan_left
    path("pan_right", views.pan_right), #when the url of the page get the /pan_right extention, run views.pan_right
    path("cam_reset", views.cam_reset) #when the url of the page get the /cam_reset extention, run views.cam_reset
] 



