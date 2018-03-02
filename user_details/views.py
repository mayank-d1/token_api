from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Token
from rest_framework import status

from .serializers import UserSerializer


class UserList(APIView):
    def get(self, request):
        user1 = User.objects.all()
        serializer = UserSerializer(user1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            token = Token(user_id=serializers.data["id"])
            token.save()
            return Response(serializers.data)
        else:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
