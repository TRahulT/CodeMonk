import json
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Paragraph, Word,CustomUser
from .serializers import ParagraphSerializer,WordSerializer,CustomUserProfileSerializer,CustomUserLoginSerializer
from rest_framework.response import Response
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.conf import settings
import jwt
from datetime import datetime, timedelta

@api_view(['GET', 'POST'])
def custom_user_create(request):
    if request.method == "GET":
        user = CustomUser.objects.all()
        serializer = CustomUserProfileSerializer(user, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CustomUserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CustomUserLoginView(APIView):
    def post(self, request, format=None):
        serializer = CustomUserLoginSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        email = serializer.validated_data['email']

        try:
            user = CustomUser.objects.get(email=email)

            if email == user.email:
                request.session['id'] = user.id

                expiration_time = datetime.utcnow() + timedelta(hours=24)
                payload = {
                    'user_id': user.id,
                    'exp': expiration_time.timestamp()
                }
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

                response = Response({
                    'token': token,
                    'message': 'CustomUser logged in successfully.',
                    'is_log': True,
                    'username': name
                }, status=status.HTTP_200_OK)
                response.set_cookie('my_jwt_cookie', token, httponly=True, secure=True, samesite="None")
                return response
            else:
                return Response({'detail': 'Invalid name or email.', 'is_loged': False},
                                status=status.HTTP_201_CREATED)

        except CustomUser.DoesNotExist:
            return Response({'detail': 'User does not exist.', 'is_loged': False}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def upload_paragraphs(request):
    user_id = getattr(request, 'user_id', None)
    if request.method == "POST":
        if user_id is not None:
             # here i'm printing the requested data

            print("Request data:", request.data)
            paragraphs = request.data.get('paragraphs', '').split('\n\n')

            # here split the data into multiple paragraphs on the basis two newline characters.
            print("Paragraphs:", paragraphs)

            # example: Paragraphs: ['Rahul is a brother ', 'anshika is my sister']

            paragraph_objs = []
            for para in paragraphs:
                if para.strip():
                    print("Paragraph:", para)
                    #example = Paragraph: Rahul is a brother
                    para_obj = Paragraph.objects.create(text=para.strip()) #here the paragraphs are stored in the Paragraph table
                    words = para.strip().lower().split()
                    print("Paragraph object:", para_obj)
                    for i in words:
                        # here word and paragraph were the keys used in Word Table
                        Word.objects.get_or_create(word=i, paragraph=para_obj)  # { get_or_create }  method instead of { create } to ensure that you're not creating duplicate Word objects.
                    paragraph_objs.append(para_obj)

            print(paragraph_objs)
            '''# it contains [
        {
        "id": 14,     ----------------->Paragraph ID
        "text": "Rahul is a boy"  -------->Paragraph TEXT
        },
        {
        "id": 15,
        "text": "anshika is my sister"
        } ]'''
            serializer = ParagraphSerializer(paragraph_objs, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET'])
def search_word(request, word):
    user_id = getattr(request, 'user_id', None)
    if request.method == "GET":
        if user_id is not None:
            input_word = word.lower()
            paragraphs = Paragraph.objects.filter(word__word=input_word).annotate(num_words=Count('word')).order_by('-num_words')[:10]
    # 'word' refers the relative_name used for Paragraph
    #__word refers to the word field in the Word model.
    # a temporary field called num_words to each paragraph, which represents the number of words in that paragraph.
    # -num_words means descending Order upto [:10]
            response_data = []
            for paragraph in paragraphs:
                response_data.append({
                    'id': paragraph.id,
                    'text': paragraph.text
                })
            return Response(response_data,status=status.HTTP_200_OK)


