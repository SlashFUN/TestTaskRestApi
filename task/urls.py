from django.urls import path
from . import views

urlpatterns = [
    path('api', views.api, ),

    path('api/users/', views.UserListCreate.as_view(), name='user_api_list'),
    path('api/users/<int:pk>', views.UserDetailUpdateDelete.as_view(), name='user_api_detail'),


    path('api/groups/', views.GroupListCreate.as_view(), name='group_api_list'),
    path('api/groups/<int:pk>', views.GroupDetailUpdateDelete.as_view(), name='group_api_detail'),
]
