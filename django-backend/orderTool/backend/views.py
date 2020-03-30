from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from backend import serializers
import json
# Create your views here.

class UserRigister(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_fields = "__all__"
    permission_classes = []
    def list(self, request, *args, **kwargs):
        return Response({"detail":"Method \"{}\" not allowed.".format(str(request.method))}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        try:
            admin = request.POST["username"]
            password = request.POST["password"]
        except:
            return Response({"detail":"Please input a username or password."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create_user(admin, admin, password)
            if "first_name" in request.POST:
                user.first_name = request.POST["first_name"]
            if "last_name" in request.POST:
                user.last_name = request.POST["last_name"]
            if "email" in request.POST:
                user.email = request.POST["email"]
            user.save()
            return Response({"detail":"OK"}, status=status.HTTP_201_CREATED)
        except:
            return Response({"detail":"User is already exist! Please change another one."}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response({"detail":"Method \"{}\" not allowed.".format(str(request.method))}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({"detail":"Method \"{}\" not allowed.".format(str(request.method))}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
class UserManager(viewsets.ModelViewSet):

    # queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_fields = "__all__"

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = User.objects.filter(pk=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs): 
        queryset = self.get_queryset()
        if int(request.user.id) != int(kwargs["pk"]):
            return Response({"detail":"Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)
        if request.method == "PUT":
            try:
                old_password = request.POST["old_password"]
                new_password = request.POST["new_password"]
            except:
                return Response({"detail":"Please input your old/new password."}, status=status.HTTP_400_BAD_REQUEST)
            user = self.get_object()
            check_user = authenticate(username=user , password=old_password)
            if check_user is None:
                return Response({"detail":"Old password wrong. Please try again."}, status=status.HTTP_400_BAD_REQUEST)
            if old_password == new_password:
                return Response({"detail":"Old password is equal to new password."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.set_password(request.POST["new_password"])
                user.save()
            return Response({"detail":"OK"}, status=status.HTTP_201_CREATED)

        elif request.method == "PATCH":
            user = self.get_object()
            if "first_name" in request.POST:
                user.first_name = request.POST["first_name"]
            if "last_name" in request.POST:
                user.last_name = request.POST["last_name"]
            if "email" in request.POST:
                user.email = request.POST["email"]
            user.save()
            return Response({"detail":"OK"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"detail":"Method \"{}\" not allowed.".format(str(request.method))}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def destroy(self, request, *args, **kwargs):
        return Response({"detail":"Method \"{}\" not allowed.".format(str(request.method))}, status=status.HTTP_405_METHOD_NOT_ALLOWED)