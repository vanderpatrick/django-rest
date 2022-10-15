from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import profileSerializer


class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = profileSerializer(profiles, many=True)

        return Response(serializer.data)
