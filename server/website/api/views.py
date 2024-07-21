from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import viewsets, parsers, status, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from . import serializers, dao, filters, mixins


@staff_member_required
def get_stats_categories(request):
    amount = [data["amount"]
              for data in dao.stats_amount_medications()]
    labels = [data["name"]
              for data in dao.stats_amount_medications()]

    return JsonResponse({
        "data":  {
            "labels": labels,
            "datasets": [{
                "data": amount,
                "label": "Amount"
            }]
        },
    })


class CategoryViewSet(mixins.BaseViewSet, viewsets.ViewSet, generics.ListAPIView):
    """
    This API returns a list of all **active** categories in the system.

    For more details on how categories are activated, please [see here](http://example.com/activating-accounts).
    """

    filename = 'categories.xlsx'
    queryset = dao.load_categories()
    serializer_class = serializers.CategorySerializer
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)


class MedicationViewSet(mixins.FOSViewSet, viewsets.ReadOnlyModelViewSet):
    """
    This API returns a list of all **active** medications in the system.

    For more details on how medications are activated, please [see here](http://example.com/activating-accounts).
    """

    filename = 'medications.xlsx'
    queryset = dao.load_medications()
    serializer_class = serializers.MedicationSerializer
    filterset_class = filters.MedicationFilter
    ordering_fields = ['price', 'name']
    search_fields = ['name']
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
    

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, slug=None):
        return Response(
            serializers.MedicationDetailSerializer(self.get_object()).data, 
            status=status.HTTP_200_OK
        )
    
    
class PatientViewSet(mixins.CreateListRetrieveUpdateViewSet):
    """
    This API returns a list of all **active** patients in the system.

    For more details on how patients are activated, please [see here](http://example.com/activating-accounts).
    """

    filename = 'patients.xlsx'
    queryset = dao.load_patients()
    serializer_class = serializers.PatientSerializer
    parser_classes = [parsers.MultiPartParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.GenericViewSet):
    queryset = dao.load_users()
    serializer_class = serializers.UserSerializer
    lookup_field = "username"

    def get_permissions(self):
        if self.action in ["forgot_password", "reset_password"]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers("Authorization"))
    @action(detail=False, methods=["get"], url_path="current-user", name="Current User")
    def current_user(self, request):
        """Get the currently logged on user."""
        return Response(serializers.CurrentUserSerializer(request.user).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["patch"], url_path="change-password", name="Change Password")
    def change_password(self, request):
        """Change password the currently logged on user."""
        user = request.user
        serializer = serializers.PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, url_path="forgot-password", name="Forgot Password")
    def forgot_password(self, request):
        """Forgot password user."""
        serializer = serializers.ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Verification email successful. Please check your inbox."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['patch'], detail=False, url_path="reset-password", name="Reset Password")
    def reset_password(self, request):
        """Reset password user."""
        serializer = serializers.ResetPasswordserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Password changed successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorViewSet(mixins.CreateListRetrieveUpdateViewSet):
    """
    This API returns a list of all **active** doctors in the system.

    For more details on how doctors are activated, please [see here](http://example.com/activating-accounts).
    """

    filename = 'doctors.xlsx'
    queryset = dao.load_doctors()
    serializer_class = serializers.DoctorSerializer
    filterset_class = filters.DoctorFilter
    ordering_fields = ['user']
    search_fields = ['user__first_name', 'user__last_name']

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request):
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
    

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, slug=None):
        return Response(
            serializers.DoctorDetailsSerializer(self.get_object()).data, 
            status=status.HTTP_200_OK
        )