from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from profiles.models import CustomUser



@api_view(['POST'])
@permission_classes([AllowAny])
def api_sign_in(request):
    """Api endpoint to sign in a user"""
    request_data = request.data
    email = request_data.get("email", None)
    password = request_data.get("password", None)
    
    if email != None and password != None:
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            data = {
                "message": "Email or password is invalid",
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except:
            data = {
                "message": "Error, unable to sign in",
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        authenticated = user.check_password(password)
        
        if authenticated != True:
            data = {
                "message": "Email or password is invalid",
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            login(request, user)
            data = {
                "message": "Login successful",
            }
            return Response(data=data, status=status.HTTP_200_OK)
    
    else:
        data = {
            "message": "Bad request, invalid email or password or both",
        }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
