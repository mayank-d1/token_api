from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Token
from rest_framework import status
from .serializers import UserSerializer


class UserList(APIView):
    def get(self, request):
        query = self.request.GET.get('token')
        us_id = self.request.GET.get('user')
        token = Token.objects.get(token=query)
        user_id = Token.objects.get(user_id=us_id)
        if token == user_id:
            user1 = User.objects.filter(id=token.user_id)
            serializer = UserSerializer(user1, many=True)
            return Response(serializer.data)
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            token = Token(user_id=serializers.data["id"])
            token.save()
            response_data = [{"token": str(token.token)}]
            return Response(response_data, status.HTTP_200_OK)
        else:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)
