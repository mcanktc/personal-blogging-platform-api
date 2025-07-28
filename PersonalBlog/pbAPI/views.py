from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PostList(APIView):
    
    def get(self, request):
        pub_date = request.query_params.get('pub_date')
        post = Post.objects.all()
        
        if pub_date:
            post = post.filter(pub_date__date=pub_date)

        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
class PostCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            return None
        
    def get(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response({'error' : 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
class PostDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        try:
            return Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            return None
        
    def delete(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response({'error' : 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        if post.author != request.user:
            return Response({'error' : 'You are not allowed to delete this post.'}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            return None
        
    def get(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response({'error' : 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        if post.author != request.user:
            return Response({'error' : 'You are not allowed to update this post.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if post is None:
            return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        if post.author != request.user:
            return Response({'error' : 'You are not allowed to update this post.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)