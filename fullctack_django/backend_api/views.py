from django.shortcuts import render
from rest_framework.views import APIView
from .models import User, Profile
from .serializer import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    RegisterSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status

# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# @api_view(["GET"])
# def getRoutes(request):
#     routes = ["/api/token/", "/api/register/", "/api/token/refresh/"]
#     return Response(routes)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == "GET":
        response = f"Hey {request.user}, You are seeing a GET response"
        return Response({"response": response}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        text = "POST IS CORRECT"
        data = f"{text}"
        return Response({"response": data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)
