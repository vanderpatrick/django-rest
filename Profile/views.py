from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import Profile
from .serializers import profileSerializer
from drf_api.permission import IsOwnerOrReadOnly

# Non refactored code
# class ProfileList(APIView):
#     def get(self, request):
#         profiles = Profile.objects.all()
#         serializer = profileSerializer(
#             profiles, many=True, context={'request': request})

#         return Response(serializer.data)


# class ProfileDetail(APIView):
#     serializer_class = profileSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = profileSerializer(profile, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = profileSerializer(
#             profile, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(generics.ListAPIView):
    serializer_class = profileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = profileSerializer
    queryset = Profile.objects.all()