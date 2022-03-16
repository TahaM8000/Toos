from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import *
from accounts.models import User
from rest_framework import status
from course.models import Grade
# REACT_APP_VALIDATION_CODE = 'fdgfdhj67867sdfsf2343nh'
danial = 'fdgfdhj67867sdfsf2343nh'

# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def get_total_code(request):
    info = GetTotalPrice(data=request.data)
    if info.is_valid():
        try:
            user = User.objects.get(phoneNumber=info.validated_data['phoneNumber'])
        except User.DoesNotExist:
            return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        total = user.cart.get_total_price()
        return Response({'total': total}, status=status.HTTP_200_OK)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def add_stuff(request,phoneNumber,code):
    try:
        course = Course.objects.get(code = code)
    except Course.DoesNotExist:
        return Response({'error': 'this course does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if user.cart is None:
        new_cart = Cart(user=user)
        user.cart = new_cart
        


    stuff = Stuff(title=course.title_persion,
    price=course.price,
    picture = course.picture,
    teacher = course.teacher.name,
    course = course,
    code = course.code,
    )
    
    stuff.cart = user.cart
    # stuff.cart.get_total_price()
    stuff.save()
    return Response({'message': 'ok is create'}, status=status.HTTP_201_CREATED)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def test(request,phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message":user.cart.get_total_price()}, status=status.HTTP_200_OK)

# ----------------------------------------------------------------------------------------------------------------------------

@api_view(['GET'])
@permission_classes([AllowAny])
def get_cart(request,phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # user.cart.get_total_price()
    # user.cart.save()
    stuff = user.cart.stuff
    data = GetCartPrice(stuff, many=True)

    return Response(data.data, status=status.HTTP_200_OK)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def get_total(request,phoneNumber):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    user.cart.save() 
    total = user.cart.get_total_price()
    count = user.cart.stuff.all().count()
    return Response({'total':total,'count':count}, status=status.HTTP_200_OK)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_stuff(request,phoneNumber,code):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    stuff_del = user.cart.stuff.filter(code=code)
    stuff_del.delete()
    
    return Response({'message': 'ok is deleted'}, status=status.HTTP_204_NO_CONTENT)
# ----------------------------------------------------------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])
def apply_coupon(request,phoneNumber,coupon):
    try:
        user = User.objects.get(phoneNumber=phoneNumber)
    except User.DoesNotExist:
        return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    try:
        input_coupon = Coupon.objects.get(code=coupon)
    except Coupon.DoesNotExist:
        return Response({'error': 'this coupon does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if(input_coupon.active):
        user.cart.coupon = input_coupon
        user.cart.save()
        user.save()
        return Response({'message': 'ok is apply'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'this coupon is not valid'}, status=status.HTTP_404_NOT_FOUND)

# ----------------------------------------------------------------------------------------------------------------------------
#Zarinpal
# from django.http import HttpResponse
# from django.shortcuts import redirect
# import requests
# import json

# MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
# ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
# ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
# # amount = 11000  # Rial / Required
# description = "دوره های اموزشی فرتاک"  # Required
# email = 'email@example.com'  # Optional
# # mobile = '09123456789'  # Optional
# # Important: need to edit for realy server.
# CallbackURL = 'http://localhost:8000/api/zarin/verify/'


# def send_request(request,phoneNumber):
#     try:
#         user = User.objects.get(phoneNumber=phoneNumber)
#     except User.DoesNotExist:
#         return Response({'error': 'this user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
#     global amount 
#     amount = user.cart.get_total_price()
    
#     result = client.service.PaymentRequest(MERCHANT, amount, description, email, user.phoneNumber, CallbackURL)
#     if result.Status == 100:
#         return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
#     else:
#         return HttpResponse('Error code: ' + str(result.Status))


# def verify(request):
#     t_status = request.GET.get('Status')
#     t_authority = request.GET['Authority']
#     if request.GET.get('Status') == 'OK':
#         req_header = {"accept": "application/json",
#                       "content-type": "application/json'"}
#         req_data = {
#             "merchant_id": MERCHANT,
#             "amount": amount,
#             "authority": t_authority
#         }
#         req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
#         if len(req.json()['errors']) == 0:
#             t_status = req.json()['data']['code']
#             if t_status == 100:
#                 return HttpResponse('Transaction success.\nRefID: ' + str(
#                     req.json()['data']['ref_id']
#                 ))
#             elif t_status == 101:
#                 return HttpResponse('Transaction submitted : ' + str(
#                     req.json()['data']['message']
#                 ))
#             else:
#                 return HttpResponse('Transaction failed.\nStatus: ' + str(
#                     req.json()['data']['message']
#                 ))
#         else:
#             e_code = req.json()['errors']['code']
#             e_message = req.json()['errors']['message']
#             return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
#     else:
#         return HttpResponse('Transaction failed or canceled by user')
# ----------------------------------------------------------------------------------------------------------------------------