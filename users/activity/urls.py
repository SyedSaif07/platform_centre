from django.urls import path
from . import views
urlpatterns = [
    path('v1/', views.list_or_create_activity, name='activitylistcreatev1'),
    path('v2/', views.ActivityListCreate.as_view(), name='activitylistcreatev2'),
    path('v3/', views.ActivityListCreateMixin.as_view(), name='activitylistcreatev3'),
    path('v4/', views.ActivityListCreateGenericAPIView.as_view(), name='activitylistcreatev4')
]