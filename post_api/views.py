from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Post
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerialzer

# Create your views here.
@api_view(['GET', 'POST'])
def postAPIView(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-id')
        post_serializer = PostSerialzer(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method == 'POST':
        post_serializer = PostSerialzer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, safe=False)
    

@api_view(['GET'])
def postDetailAPIView(request,id=None):
    post = get_object_or_404(Post, id=id)
    print(post)
    post_serializer = PostSerialzer(post)
    return JsonResponse(post_serializer.data, safe=False)



@api_view(['GET','PUT'])
def postDetailUpdateAPIView(request,id=None):
    if request.method == 'PUT':
        post = get_object_or_404(Post, id=id)
        post_serializer = PostSerialzer(instance=post, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, safe=False)

    elif request.method == 'GET':
        post = get_object_or_404(Post,id=id)
        post_serializer = PostSerialzer(post)
        return JsonResponse(post_serializer.data, safe=False)


@api_view(['GET', 'DELETE'])
def postDeletePIView(request,id=None):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, id=id)
        post.delete()

    if request.method == 'GET':
        post = get_object_or_404(Post, id=id)
        post_serializer = PostSerialzer(post)
        return JsonResponse(post_serializer.data, safe=False)

#user API Views
@api_view(['GET', 'POST'])
def userAPIView(request):
    if request.method =='GET':
        users = User.objects.all().order_by('-id')
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, safe=False)


        
        

