from django.forms import model_to_dict
from .serializers import CustomUserSerializer, Model3dSerializer, BadgeSerializer
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Model3d, Badge, CustomUser
from .utils import check_collector_badge, check_pioneer_badge, check_star_badge
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class Model3dViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Model3d.objects.all()
    serializer_class = Model3dSerializer

class BadgeViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer



# @api_view(['POST'])
# def create_user(request):
#     username = request.data.get('username')
#     email = request.data.get('email')
#     password = request.data.get('password')
#     user = CustomUser.objects.create_user(username, email, password)
#     return JsonResponse({'message': f'User {username} created successfully'})


# @api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def upload_model(request, user_id):
#     views = request.data.get('views')
#     image_url = request.data.get('image_url')
#     user = CustomUser.objects.get(id=user_id)
#     model = Model3d.objects.create(user=user, views=views, image_url=image_url)
#     check_collector_badge(user_id)
#     check_pioneer_badge(user_id, user.date_joined)
#     check_star_badge(user_id, model.id)
#     return JsonResponse({'message': 'Model uploaded successfully'})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def user_badges(request, user_id):
    badges = Badge.objects.filter(user_id=user_id)
    badges_list = list(badges.values())
    return JsonResponse(badges_list, safe=False)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def star_badge(request, user_id, model_id):
    check_star_badge(user_id, model_id)
    return JsonResponse({'message': 'Star badge awarded'})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def collector_badge(request, user_id):
    check_collector_badge(user_id)
    return JsonResponse({'message': 'Collector badge awarded'})

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def pioneer_badge(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    check_pioneer_badge(user_id,user.date_joined )
    return JsonResponse({'message': 'Pioneer badge awarded'})
