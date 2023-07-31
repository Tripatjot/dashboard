from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Role
from .serializers import UserSerializer

# Create your views here.
class create_user(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        role_data = request.data.get('role')
        role_status = request.data.get('status')

        try:
            role_instance = Role.objects.create(role=role_data, status=role_status)
            if serializer.is_valid():
                serializer.save(role = role_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class get_users(APIView):
    def get(self, request, pk):
        users = User.objects.filter(role__role=pk)
        if not users.exists():
            return Response("ERROR: Users do not exist", status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

class update_user(APIView):
    def put (self, request, pk):
        user = User.objects.get(id = pk)
        serializer = UserSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class delete_user(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            print(user.role.status)
            user.role.status = 1 if user.role.status == 0 else 0
            user.role.save()
            return Response({'message': 'User status changed to ' + str(user.role.status)})
        except User.DoesNotExist:
            return Response("ERROR: User does not exist", status=status.HTTP_400_BAD_REQUEST)