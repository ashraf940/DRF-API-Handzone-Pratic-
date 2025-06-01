from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets, status

from home.models import People
from home.serializers import PeopleSerializer
from .serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from django.core.paginator import Paginator

# ----------------------------
# Authentication APIs
# ----------------------------

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=401)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'status': True,
            'token': token.key,
            'message': 'Login Successful'
        }, status=200)


class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data, status=201)

# ----------------------------
# Sample Test API
# ----------------------------

@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['Flask', 'Django', 'FastAPI'],
        'course_provider': 'Scaler'
    }
    if request.method == 'GET':
        print(request.GET.get('search'))
        return Response(courses)
    elif request.method == 'POST':
        print(request.data.get('age'))
        return Response(courses)
    elif request.method == 'PUT':
        return Response(courses)

# ----------------------------
# People Class-Based API (with Auth & Pagination)
# ----------------------------

class PersonAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            objs = People.objects.all()
            page = request.GET.get('page', 1)
            page_size = 3
            paginator = Paginator(objs, page_size)
            serializer = PeopleSerializer(paginator.page(page), many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=500)

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        try:
            obj = People.objects.get(id=request.data.get('id'))
        except People.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        serializer = PeopleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request):
        try:
            obj = People.objects.get(id=request.data.get('id'))
        except People.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        serializer = PeopleSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        try:
            obj = People.objects.get(id=request.data.get('id'))
        except People.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        obj.delete()
        return Response({'message': 'Person Deleted successfully'}, status=200)

# ----------------------------
# Alternative Function-Based View (Optional)
# ----------------------------

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = People.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        try:
            obj = People.objects.get(id=request.data.get('id'))
        except People.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        serializer = PeopleSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        try:
            obj = People.objects.get(id=request.data.get('id'))
        except People.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        serializer = PeopleSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            obj = People.objects.get(id=request.data.get('id'))
        except People.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        obj.delete()
        return Response({'message': 'Person Deleted successfully'})

# ----------------------------
# ViewSet with Filtering & Action
# ----------------------------

class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = People.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)
        serializer = PeopleSerializer(queryset, many=True)
        return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def send_mail_to_person(self, request, pk):
        try:
            obj = People.objects.get(pk=pk)
        except People.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

        serializer = PeopleSerializer(obj)
        # TODO: Add email sending logic here
        return Response({
            'status': True,
            'message': 'Mail Sent Successfully',
            'data': serializer.data
        }, status=200)
