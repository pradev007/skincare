# account/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer
from .permissions import IsSuperAdmin,IsUser,IsVendor
import logging


logger = logging.getLogger(__name__)

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"User registered: {serializer.validated_data['fullname']} ({serializer.validated_data['role']})")
            return Response({"message":"User created successfully"}, status=status.HTTP_201_CREATED)
        logger.error(f"Registration failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception = True)
        except Exception as e:
            logger.error(f"Login failed :{str(e)}")
            return Response({'error':str(e)},status=status.HTTP_401_UNAUTHORIZED)
        logger.info(f"Login successfull: {serializer.validated_data['fullname']} {serializer.validated_data['role']}")
        return Response(serializer.validated_data,status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"User logged out: {request.user.fullname}")
            return Response({"message":"Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Logout failed: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class VendorDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsVendor]
    def get(self,request):
        return Response({"message":f"Welcome to the vendor dashboard, {request.user.fullname}!"}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    permission_classes = [IsUser]

    def get(self,request):
        return Response({"message":"welcome to your user profile, {request.user.fullname}!"},status=status.HTTP_200_OK) 

class AdminPanelView(APIView):
    permission_classes = [IsAuthenticated,IsSuperAdmin]
    def post(self,request):
        return Response({"message": f"Welcome to Admin Panel {request.user.fullname}!"}, status=status.HTTP_200_OK)
    