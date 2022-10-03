from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.views.decorators.csrf import csrf_exempt

connection = mail.get_connection()
@csrf_exempt
@api_view(['GET'])
def overAPIView(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@csrf_exempt
@api_view(['POST'])
def ResponesData(request):
    connection.open()
    send_mail(
        'Ét ô ét!',
        'trời ơi tế cái rụp rồi',
        settings.EMAIL_HOST_USER,
        ['ntdang_20th@student.agu.edu.vn'],
        connection=connection,
    )
    connection.close()
    return Response(request.data)
