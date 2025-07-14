# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from .permissions import IsVendor, IsUser, IsSuperAdmin
import logging

# Set up logging for login, registration, and logout attempts
logger = logging.getLogger(__name__)

class RegisterView(APIView):
    """
    API view to handle user registration for users and vendors.
    Allows unauthenticated access for registration.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"User registered: {serializer.validated_data['fullname']} ({serializer.validated_data['role']})")
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        logger.error(f"Registration failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(TokenObtainPairView):
    """
    API view for JWT login using fullname and password, returning role in response.
    Allows unauthenticated access for login.
    """
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            logger.info(f"Login successful: {serializer.validated_data['fullname']} ({serializer.validated_data['role']})")
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Login failed: {str(e)}")
            return Response({"error": "Invalid credentials or account inactive"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    """
    API view to blacklist JWT refresh token for logout.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"User logged out: {request.user.fullname}")
            return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger.error(f"Logout failed: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VendorDashboardView(APIView):
    """
    Protected view for vendors only.
    Requires authentication and vendor role.
    """
    permission_classes = [IsAuthenticated, IsVendor]

    def get(self, request):
        return Response({"message": f"Welcome to the Vendor Dashboard, {request.user.fullname}!"}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    """
    Protected view for users only.
    Requires authentication and user role.
    """
    permission_classes = [IsAuthenticated, IsUser]

    def get(self, request):
        return Response({"message": f"Welcome to your User Profile, {request.user.fullname}!"}, status=status.HTTP_200_OK)

class AdminPanelView(APIView):
    """
    Protected view for superadmins only.
    Requires authentication and superadmin role.
    """
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        return Response({"message": f"Welcome to the Admin Panel, {request.user.fullname}!"}, status=status.HTTP_200_OK)