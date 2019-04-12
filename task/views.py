from rest_framework.filters import SearchFilter
from .serializers import *
from rest_framework import generics
from django.http import JsonResponse
from django.middleware.csrf import get_token


class UserListCreate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('username', 'email')


class UserDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class GroupListCreate(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class GroupDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


def ping(request):
    return JsonResponse({'result': 'OK'})


def api(request):
    return JsonResponse({'result': 'HUJ'})
