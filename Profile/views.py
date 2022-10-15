from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import profileSerializer


class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = profileSerializer(profiles, many=True)

        return Response(serializer.data)


class ProfileDetail(APIView):
    serializer_class = profileSerializer
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = profileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = profileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)