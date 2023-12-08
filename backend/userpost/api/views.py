from rest_framework.views import APIView
from rest_framework import status,viewsets
from userpost.models import Posts
from rest_framework.response import Response
from userpost.api.serializers import PostSerializer
from rest_framework.generics import RetrieveAPIView



class CreatePostViewSet(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
class UserPosts(APIView):
    def get(self, request):
        try:
            queryset = Posts.objects.all()
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
        except Posts.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
   